#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import errno
import json
import os
import re
import tempfile

from subprocess import Popen, PIPE

from ansible.module_utils.common.text.converters import to_bytes, to_native
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
module: onepassword_info
author:
    - Oscar Hermosa <osmollo@proton.me>
requirements:
    - C(op) 1Password command line utility. See U(https://support.1password.com/command-line/)
notes:
    - Tested with C(op) version 2.7.3
options:
    name:
        type: str
        description:
            - The name of the 1Password item to search for
    id:
        type: str
        description:
            - The id of the 1Password item to search for
    label:
        type: str
        description:
            - The name of the label to search for within this item (optional, defaults to "password" (or "document" if the item has an attachment).
            - If is set to 'all', returns the whole item
    vault:
        type: str
        description:
            - The name of the particular 1Password vault to search, useful if your 1Password user has access to multiple vaults (optional).
        required: true
    cli_path:
        type: path
        description: Used to specify the exact path to the C(op) command line interface
        required: false
        default: 'op'
'''

EXAMPLES = '''
# Gather secrets from 1Password, assuming there is a 'password' label:
- name: Get a password
  onepassword:
    name: My 1Password item
  delegate_to: localhost
  register: my_1password_item
  no_log: true         # Don't want to log the secrets to the console!

# Gather secrets from 1Password, with more advanced search terms:
- name: Get a password
  onepassword:
    name:    My 1Password item
    label:   Custom label name       # optional, defaults to 'password'
    vault:   Name of the vault       # optional, only necessary if there is more than 1 Vault available
  delegate_to: localhost
  register: my_1password_item
  no_log: true                           # Don't want to log the secrets to the console!

- name: Debug a password (for example)
  ansible.builtin.debug:
    msg: "{{ my_1password_item['onepassword']['My 1Password item'] }}"
'''

RETURN = '''
---
# One or more dictionaries for each matching item from 1Password, along with the appropriate labels.
# This shows the response you would expect to receive from the third example documented above.
onepassword:
    description: Dictionary of each 1password item matching the given search terms, shows what would be returned from the third example above.
    returned: success
    type: dict
    sample:
        "My 1Password item":
            password: the value of this label
            Custom label name: the value of this label
'''


class OnePasswordConfig(object):
    _config_file_paths = (
        "~/.op/config",
        "~/.config/op/config",
        "~/.config/.op/config",
    )

    def __init__(self):
        self._config_file_path = ""

    @property
    def config_file_path(self):
        if self._config_file_path:
            return self._config_file_path

        for path in self._config_file_paths:
            realpath = os.path.expanduser(path)
            if os.path.exists(realpath):
                self._config_file_path = realpath
                return self._config_file_path


class AnsibleModuleError(Exception):
    def __init__(self, results):
        self.results = results

    def __repr__(self):
        return self.results


class OnePasswordInfo(object):

    def __init__(self):
        self.cli_path = module.params.get('cli_path')
        self.logged_in = False
        self.token = None

        self.name = module.params.get('name')
        self.id = module.params.get('id')
        self.label = module.params.get('label')
        self.vault = module.params.get('vault')

        self._config = OnePasswordConfig()

    def _run(self, args, expected_rc=0, command_input=None, ignore_errors=False):
        if self.token:
            # Adds the session token to all commands if we're logged in.
            args += [to_bytes('--session=') + self.token]

        command = [self.cli_path] + args
        p = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        out, err = p.communicate(input=command_input)
        rc = p.wait()
        if not ignore_errors and rc != expected_rc:
            raise AnsibleModuleError(to_native(err))
        return rc, out, err

    def _parse_label(self, data_json, item_id, label_name):
        """
        Retrieves the desired label from the `op` response payload

        The password is within a labels array:

        $ op get item 'test item' | jq
        {
          [...]
          "fields": [
            {
              "id": "username",
              "label": "username",
              "type": "STRING",
              "value": "foo"
            },
            {
              "id": "password",
              "label": "password",
              "type": "CONCEALED",
              "value": "bar"
            },
            {
              "id": "sdfsdf",
              "section": {
                "id": "asdasd",
                "label": "section name"
              }
            }
          ],
          [...]
        """
        data = json.loads(data_json)

        for label_data in data.get('fields', []):
            if label_data.get('label', '').lower() == label_name.lower():
                return label_data.get('value', '')
        if data['category'] == 'DOCUMENT':
            for label_data in data.get('files', []):
                if label_name.lower() in label_data:
                    return label_data.get(label_name.lower(), '')
        return ''

    def get_raw(self, item_id, vault=None):
        args = ["item", "get", item_id, "--format", "json"]
        if vault is not None:
            args += ['--vault={0}'.format(vault)]
        _, output, _ = self._run(args)
        return output

    def get_label(self, item_name=None, item_id=None, label=None, vault=None):
        if item_name:
            data = self.get_raw(item_name, vault)
            if label != 'all':
                output = self._parse_label(data, item_name, label)
            else:
                output = json.loads(data)
        elif item_id:
            data = self.get_raw(item_id, vault)
            if label != 'all':
                output = self._parse_label(data, item_id, label)
            else:
                output = json.loads(data)
        return output if output != '' else ''

    def assert_logged_in(self):
        try:
            rc, _, _ = self._run(['account', 'get'], ignore_errors=True)
            if rc == 0:
                self.logged_in = True
        except OSError as e:
            if e.errno == errno.ENOENT:
                module.fail_json(msg="1Password CLI tool '%s' not installed in path on control machine" % self.cli_path)
            raise e

    def run(self):
        self.assert_logged_in()
        return self.get_label(item_name=self.name, item_id=self.id,
                              label=self.label, vault=self.vault)


def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            cli_path=dict(type='path', default='op'),
            name=dict(type='str', default=None),
            id=dict(type='str', default=None),
            label=dict(type='str', default='password'),
            vault=dict(type='str', default='Personal')
        ),
        supports_check_mode=True
    )

    if 'name' not in module.params and 'id' not in module.params:
        module.fail_json(msg="'id' or 'name' argument is required")
    else:
        results = {'onepassword': OnePasswordInfo().run()}
        module.exit_json(changed=False, **results)


if __name__ == '__main__':
    main()
