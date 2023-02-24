from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import errno
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
    short_description: fetch field values from 1Password that matches with specified label
    description:
      - C(onepassword) wraps the C(op) command line utility to fetch specific label values from 1Password.
    options:
      _term:
        description: reference of item to retrieve.
        required: true

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
- name: Retrieve password for reference
  ansible.builtin.debug:
    var: lookup('onepassword', 'op://foo/bar/item/section/id')
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

    def get_raw(self, reference):
        args = ["read", reference]
        _, output, _ = self._run(args)
        output = output.decode("utf-8")
        return output[:-1] if output.endswith('\n') else output

    def get_field(self, reference):
        return self.get_raw(reference)

    def _run(self, args, expected_rc=0, command_input=None, ignore_errors=False):
        command = [self.cli_path] + args
        p = Popen(command, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        out, err = p.communicate(input=command_input)
        rc = p.wait()
        if not ignore_errors and rc != expected_rc:
            raise AnsibleLookupError(to_text(err))
        return rc, out, err


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        op = OnePass()
        op.assert_logged_in()

        values = []
        for term in terms:
            values.append(op.get_field(term))

        return values
