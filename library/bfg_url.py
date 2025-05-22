#!/usr/bin/python

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
module: bfg_url

short_description: return the url of latest BFG version
                   parsing the url 'https://rtyley.github.io/bfg-repo-cleaner/#usage'

version_added: "2.5"

description:
    - "return the url of latest BFG version parsing
    the url https://rtyley.github.io/bfg-repo-cleaner/#usage"

author:
    - Oscar Hermosa (osmollo@proton.me)
'''

EXAMPLES = '''
# Get latest version of BFG
- name: "get BFG url"
  bfg_url:
  register: bfg_response

- debug: var=bfg_response.url
'''

RETURN = '''
version:
    description: The latest version of BFG
    type: string
    returned: always
'''


def get_url():
    bfg_url = "https://rtyley.github.io/bfg-repo-cleaner/#usage"
    bfg_text = requests.get(bfg_url)

    if bfg_text.status_code == 200:
        soup = BeautifulSoup(bfg_text.text, 'html.parser')
        for item in soup.find_all("a", class_="button latest-download-link"):
            return item["href"]
    else:
        return None


def run_module():
    result = dict(
        changed=False,
        url=str
    )

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    result['url'] = get_url()
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
