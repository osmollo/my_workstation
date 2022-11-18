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
    search_terms:
        type: list
        elements: dict
        description:
            - A list of one or more search terms.
            - Each search term can either be a simple string or it can be a dictionary for more control.
            - When passing a simple string, I(field) is assumed to be C(password).
            - When passing a dictionary, the following fields are available.
        suboptions:
            name:
                type: str
                description:
                    - The name of the 1Password item to search for (required).
            field:
                type: str
                description:
                    - The name of the field to search for within this item (optional, defaults to "password" (or "document" if the item has an attachment).
            section:
                type: str
                description:
                    - The name of a section within this item containing the specified field (optional, will search all sections if not specified).
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
# Gather secrets from 1Password, assuming there is a 'password' field:
- name: Get a password
  community.general.onepassword_info:
    search_terms:
        - name: My 1Password item
  delegate_to: localhost
  register: my_1password_item
  no_log: true         # Don't want to log the secrets to the console!

# Gather secrets from 1Password, with more advanced search terms:
- name: Get a password
  community.general.onepassword_info:
    search_terms:
      - name:    My 1Password item
        field:   Custom field name       # optional, defaults to 'password'
        section: Custom section name     # optional, defaults to 'None'
        vault:   Name of the vault       # optional, only necessary if there is more than 1 Vault available
  delegate_to: localhost
  register: my_1password_item
  no_log: true                           # Don't want to log the secrets to the console!

# Gather secrets combining simple and advanced search terms to retrieve two items, one of which we fetch two
# fields. In the first 'password' is fetched, as a field name is not specified (default behaviour) and in the
# second, 'Custom field name' is fetched, as that is specified explicitly.
- name: Get a password
  community.general.onepassword_info:
    search_terms:
      - My 1Password item                # 'name' is optional when passing a simple string...
      - name: My Other 1Password item    # ...but it can also be set for consistency
      - name:    My 1Password item
        field:   Custom field name       # optional, defaults to 'password'
        section: Custom section name     # optional, defaults to 'None'
        vault:   Name of the vault       # optional, only necessary if there is more than 1 Vault available
      - name: A 1Password item with document attachment
  delegate_to: localhost
  register: my_1password_item
  no_log: true                           # Don't want to log the secrets to the console!

- name: Debug a password (for example)
  ansible.builtin.debug:
    msg: "{{ my_1password_item['onepassword']['My 1Password item'] }}"
'''

RETURN = '''
---
# One or more dictionaries for each matching item from 1Password, along with the appropriate fields.
# This shows the response you would expect to receive from the third example documented above.
onepassword:
    description: Dictionary of each 1password item matching the given search terms, shows what would be returned from the third example above.
    returned: success
    type: dict
    sample:
        "My 1Password item":
            password: the value of this field
            Custom field name: the value of this field
        "My Other 1Password item":
            password: the value of this field
        "A 1Password item with document attachment":
            document: the path where the document attached has been downloaded
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

        terms = module.params.get('search_terms')
        self.terms = self.parse_search_terms(terms)

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

    def _parse_field(self, data_json, item_id, field_name, section_title=None):
        data = json.loads(data_json)

        if data.get('category', '') == 'DOCUMENT':
            # This is actually a document, let's fetch the document data instead!
            dirpath = tempfile.mkdtemp()
            document_path = os.path.join(dirpath, data['files'][0]['name'])
            _ = self._run(["document", "get", data['title'], '--output', document_path])
            return {'document': document_path}

        else:
            for field_data in data['fields']:
                if field_data['id'] == field_name:
                    return {field_name: field_data.get('value', '')}
            # # This is not a document, let's try to find the requested field

            # # Some types of 1Password items have a 'password' field directly alongside the 'fields' attribute,
            # # not inside it, so we need to check there first.
            # if (field_name in data['details']):
            #     return {field_name: data['details'][field_name]}

            # # Otherwise we continue looking inside the 'fields' attribute for the specified field.
            # else:
            #     if section_title is None:
            #         for field_data in data['details'].get('fields', []):
            #             if field_data.get('name', '').lower() == field_name.lower():
            #                 return {field_name: field_data.get('value', '')}

            #     # Not found it yet, so now lets see if there are any sections defined
            #     # and search through those for the field. If a section was given, we skip
            #     # any non-matching sections, otherwise we search them all until we find the field.
            #     for section_data in data['details'].get('sections', []):
            #         if section_title is not None and section_title.lower() != section_data['title'].lower():
            #             continue
            #         for field_data in section_data.get('fields', []):
            #             if field_data.get('t', '').lower() == field_name.lower():
            #                 return {field_name: field_data.get('v', '')}

        # We will get here if the field could not be found in any section and the item wasn't a document to be downloaded.
        optional_section_title = '' if section_title is None else " in the section '%s'" % section_title
        module.fail_json(msg="Unable to find an item in 1Password named '%s' with the field '%s'%s." % (item_id, field_name, optional_section_title))

    def parse_search_terms(self, terms):
        processed_terms = []

        for term in terms:
            if not isinstance(term, dict):
                term = {'name': term}

            if 'name' not in term:
                module.fail_json(msg="Missing required 'name' field from search term, got: '%s'" % to_native(term))

            term['field'] = term.get('field', 'password')
            term['section'] = term.get('section', None)
            term['vault'] = term.get('vault', None)

            processed_terms.append(term)

        return processed_terms

    def get_raw(self, item_id, vault=None):
        try:
            args = ["item", "get", item_id, "--format", "json"]
            if vault is not None:
                args += ['--vault={0}'.format(vault)]
            rc, output, dummy = self._run(args)
            return output

        except Exception as e:
            if re.search(".*not found.*", to_native(e)):
                module.fail_json(msg="Unable to find an item in 1Password named '%s'." % item_id)
            else:
                module.fail_json(msg="Unexpected error attempting to find an item in 1Password named '%s': %s" % (item_id, to_native(e)))

    def get_field(self, item_id, field, section=None, vault=None):
        output = self.get_raw(item_id, vault)
        return self._parse_field(output, item_id, field, section) if output != '' else ''

    def assert_logged_in(self):
        try:
            rc, out, err = self._run(['account', 'get'], ignore_errors=True)
            if rc == 0:
                self.logged_in = True
        except OSError as e:
            if e.errno == errno.ENOENT:
                module.fail_json(msg="1Password CLI tool '%s' not installed in path on control machine" % self.cli_path)
            raise e

    def run(self):
        result = {}

        self.assert_logged_in()

        for term in self.terms:
            value = self.get_field(term['name'], term['field'], term['section'], term['vault'])

            if term['name'] in result:
                # If we already have a result for this key, we have to append this result dictionary
                # to the existing one. This is only applicable when there is a single item
                # in 1Password which has two different fields, and we want to retrieve both of them.
                result[term['name']].update(value)
            else:
                # If this is the first result for this key, simply set it.
                result[term['name']] = value

        return result


def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            cli_path=dict(type='path', default='op'),
            search_terms=dict(required=True, type='list', elements='dict'),
        ),
        supports_check_mode=True
    )

    results = {'onepassword': OnePasswordInfo().run()}

    module.exit_json(changed=False, **results)


if __name__ == '__main__':
    main()
