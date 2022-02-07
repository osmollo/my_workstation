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
module: get_go_latest

short_description: return the latest version of go parsing the url https://golang.org/dl

version_added: "2.5"

description:
    - "return the latest version of go parsing the url https://golang.org/dl"

author:
    - Oscar Hermosa (ohermosa@gmail.com)
'''

EXAMPLES = '''
# Get latest version of go
- name: "get go version"
  get_go_latest:
  register: go_response

- debug: var=go_response.version
'''

RETURN = '''
version:
    description: The latest version of go language
    type: string
    returned: always
'''


def get_latest():
    go_url = "https://golang.org/dl"
    go_text = requests.get(go_url)

    if go_text.status_code == 200:
        soup = BeautifulSoup(go_text.text, 'html.parser')
        for item in soup.find_all("a", class_="download"):
            if "linux-amd64.tar.gz" in item["href"]:
                return os.path.basename(item["href"])[2:].replace('.linux-amd64.tar.gz', '')
    else:
        return None


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
