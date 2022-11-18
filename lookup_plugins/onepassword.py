from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import errno
import json
import os

from subprocess import Popen, PIPE

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleLookupError
from ansible.module_utils.common.text.converters import to_bytes, to_text


DOCUMENTATION = '''
    name: onepassword
    author:
      - Oscar Hermosa (@osmollo)
    requirements:
      - C(op) 1Password command line utility. See U(https://support.1password.com/command-line/)
    short_description: fetch field values from 1Password
    description:
      - C(onepassword) wraps the C(op) command line utility to fetch specific field values from 1Password.
    options:
      _terms:
        description: identifier(s) (UUID, name, or subdomain; case-insensitive) of item(s) to retrieve.
        required: true
      field:
        description: field to return from each matching item (case-insensitive).
        default: 'password'
      vault:
        description: Vault containing the item to retrieve (case-insensitive). If absent will search all vaults.
    notes:
      - This lookup will use an existing 1Password session if one exists. If not, and you have already
        performed an initial sign in (meaning C(~/.op/config), C(~/.config/op/config) or C(~/.config/.op/config) exists), then only the
        C(master_password) is required. You may optionally specify C(subdomain) in this scenario, otherwise the last used subdomain will be used by C(op).
      - Due to the B(very) sensitive nature of these credentials, it is B(highly) recommended that you only pass in the minimal credentials
        needed at any given time. Also, store these credentials in an Ansible Vault using a key that is equal to or greater in strength
        to the 1Password master password.
      - This lookup stores potentially sensitive data from 1Password as Ansible facts.
        Facts are subject to caching if enabled, which means this data could be stored in clear text
        on disk or in a database.
      - Tested with C(op) version 2.7.3
'''

EXAMPLES = """
# These examples only work when already signed in to 1Password
- name: Retrieve password for KITT when already signed in to 1Password
  ansible.builtin.debug:
    var: lookup('community.general.onepassword', 'KITT')

- name: Retrieve password for Wintermute when already signed in to 1Password
  ansible.builtin.debug:
    var: lookup('community.general.onepassword', 'Tessier-Ashpool')

- name: Retrieve username for HAL when already signed in to 1Password
  ansible.builtin.debug:
    var: lookup('community.general.onepassword', 'HAL 9000', field='username', vault='Discovery')
"""

RETURN = """
  _raw:
    description: field data requested
    type: list
    elements: str
"""


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


class OnePass(object):
    def __init__(self, path='op'):
        self.cli_path = path
        self.logged_in = False
        self._config = OnePasswordConfig()

    def assert_logged_in(self):
        try:
            rc, out, err = self._run(['account', 'get'], ignore_errors=True)
            if rc == 0:
                self.logged_in = True
        except OSError as e:
            if e.errno == errno.ENOENT:
                raise AnsibleLookupError("1Password CLI tool '%s' not installed in path on control machine" % self.cli_path)
            raise e

    def get_raw(self, item_id, vault=None):
        args = ["item", "get", item_id, "--format", "json"]
        if vault is not None:
            args += ['--vault={0}'.format(vault)]
        _, output, dummy = self._run(args)
        return output

    def get_field(self, item_id, field, vault=None):
        output = self.get_raw(item_id, vault)
        return self._parse_field(output, field) if output != '' else ''

    def _run(self, args, expected_rc=0, command_input=None, ignore_errors=False):
        command = [self.cli_path] + args
        p = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        out, err = p.communicate(input=command_input)
        rc = p.wait()
        if not ignore_errors and rc != expected_rc:
            raise AnsibleLookupError(to_text(err))
        return rc, out, err

    def _parse_field(self, data_json, field_name):
        """
        Retrieves the desired field from the `op` response payload

        The password is within a fields array:

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

        for field_data in data.get('fields', []):
            if field_data.get('label', '').lower() == field_name.lower():
                return field_data.get('value', '')
        if data['category'] == 'DOCUMENT':
            for field_data in data.get('files', []):
                if field_name.lower() in field_data:
                    return field_data.get(field_name.lower(), '')
        return ''


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        op = OnePass()

        field = kwargs.get('field', 'password')
        vault = kwargs.get('vault')
        op.assert_logged_in()

        values = []
        for term in terms:
            values.append(op.get_field(term, field, vault))

        return values
