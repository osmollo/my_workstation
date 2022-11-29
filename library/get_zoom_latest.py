#!/usr/bin/python

import re
import requests
from bs4 import BeautifulSoup
from packaging import version
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: get_zoom_latest

short_description: return the latest version of zoom client parsing the url https://support.zoom.us/hc/en-us/articles/205759689

version_added: "2.5"

description:
    - "return the latest version of zoom client parsing the url https://support.zoom.us/hc/en-us/articles/205759689"

author:
    - Oscar Hermosa (ohermosa@gmail.com)
'''

EXAMPLES = '''
# Get latest version of zoom
- name: "get zoom version"
  get_zoom_latest:
  register: zoom_response

- debug: var=zoom_response.version
'''

RETURN = '''
version:
    description: The latest version of zoom language
    type: string
    returned: always
'''


def get_fucking_latest(versions=[]):
    r = re.compile("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$")
    stable_versions = list(filter(r.match, versions))
    for n, i in enumerate(stable_versions):
        stable_versions[n] = version.parse(i)
    return max(stable_versions).base_version


def get_latest():
    zoom_url = "https://support.zoom.us/hc/en-us/articles/205759689"
    zoom_text = requests.get(zoom_url)

    if zoom_text.status_code == 200:
        soup = BeautifulSoup(zoom_text.text, 'html.parser')
        for item in soup.find_all("strong"):
            if len(item.text) > 0 and item.text[0].isdigit():
                return item.text
        return None
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
