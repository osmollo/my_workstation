#!/usr/bin/python

import requests
import os.path
from bs4 import BeautifulSoup
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: get_1p_latest

short_description: return the latest version of 1password cli parsing the url https://app-updates.agilebits.com/product_history/CLI

version_added: "2.5"

description:
    - "return the latest version of 1password cli parsing the url https://app-updates.agilebits.com/product_history/CLI"

author:
    - Oscar Hermosa (ohermosa@gmail.com)
'''

EXAMPLES = '''
# Get latest version of 1password cli
- name: "get 1p cli version"
  get_1p_latest:
  register: get_response

- debug: var=get_response.version
'''

RETURN = '''
version:
    description: The latest version of 1password cli
    type: string
    returned: always
'''


def get_latest():
    cli1p_url = "https://app-updates.agilebits.com/product_history/CLI"
    cli1p_text = requests.get(cli1p_url)

    if cli1p_text.status_code == 200:
        soup = BeautifulSoup(cli1p_text.text, 'html.parser')
        get_linux = soup.find_all('p', class_='system linux')[0]
        return get_linux.find_all('a', title='Download for amd64')[0]['href'].split('/')[7]
    else:
        return get_latest()


def run_module():
    result = dict(
        changed=False,
        version=str
    )

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    result['version'] = get_latest()
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
