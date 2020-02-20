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
module: get_nomachine_latest

short_description: return the latest version of nomachine
                   parsing the url https://www.nomachine.com/download/download&id=5

version_added: "2.5"

description:
    - "return the latest version of nomachine parsing
      the url https://www.nomachine.com/download/download&id=5"

author:
    - Oscar Hermosa (ohermosa@gmail.com)
'''

EXAMPLES = '''
# Get latest version of nomachine
- name: "get nomachine version"
  get_nomachine_latest:
  register: nomachine_response

- debug: var=nomachine_response.version
'''

RETURN = '''
version:
    description: The latest version of nomachine
    type: string
    returned: always
'''


def get_latest():
    nomachine_url = "https://www.nomachine.com/download/download&id=5"
    nomachine_text = requests.get(nomachine_url)

    if nomachine_text.status_code == 200:
        soup = BeautifulSoup(nomachine_text.text, 'html.parser')
        return soup.find_all("div", class_="sec_cell dis_cell")[0].text.replace('\n', '')
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
