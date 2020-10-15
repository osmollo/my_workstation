#!/usr/bin/python

import re
import requests
from bs4 import BeautifulSoup
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: get_dropbox_latest

short_description: return the latest version of dropbox
                   parsing the url https://linux.dropbox.com/packages/{{ distro }}

version_added: "2.5"

description:
    - "return the latest version of dropbox parsing
      the url https://linux.dropbox.com/packages/{{ distro }}"

author:
    - Oscar Hermosa (ohermosa@gmail.com)
'''

EXAMPLES = '''
# Get latest version of dropbox
- name: "get dropbox version"
  get_dropbox_latest:
    distro: "ubuntu"
    arch: "x86_64"
  register: dropbox_response

- debug: var=dropbox_response.version
'''

RETURN = '''
version:
    description: The latest version of dropbox
    type: string
    returned: always
'''


def major_minor_micro(version):
    major, minor, micro = re.search('(\d+)\.(\d+)\.(\d+)', version).groups()
    return int(major), int(minor), int(micro)


def get_latest(distro, arch):
    dropbox_url = "https://linux.dropbox.com/packages/{}".format(distro)
    dropbox_text = requests.get(dropbox_url)
    tmparch = "amd64" if arch == "x86_64" else "i386"

    if dropbox_text.status_code == 200:
        soup = BeautifulSoup(dropbox_text.text, 'html.parser')
        versions = []
        for item in soup.find_all("a"):
            if distro == "ubuntu":
                if item.text.startswith('dropbox_') and tmparch in item.text:
                    tmpver = item.text.split('_')[1]
                    versions.append(tmpver)
            elif distro == "fedora":
                if item.text.startswith('nautilus-dropbox-'):
                    tmpver = item.text.split('-')[2]
                    versions.append(tmpver)
        if len(versions) == 0:
            return None
        else:
            return max(versions, key=major_minor_micro)
    else:
        return None


def run_module():
    fields = {
        "distro": {
            "required": True,
            "type": "str",
            "choices": ['ubuntu', 'fedora'],
        },
        "arch": {
            "default": 'x86_64',
            "type": "str",
            "choices": ['x86_64', 'i386']
        }
    }

    result = dict(
        changed=False,
        version=str
    )

    module = AnsibleModule(
        argument_spec=fields,
        supports_check_mode=True
    )

    result['version'] = get_latest(module.params['distro'], module.params['arch'])
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
