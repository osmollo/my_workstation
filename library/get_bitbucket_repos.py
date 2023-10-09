#!/usr/bin/python

import requests
from ansible.module_utils.basic import AnsibleModule
from requests.auth import HTTPBasicAuth


ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: get_bitbucket_repos

short_description: returns the 'clone string' for all repositories of all projects that users can read

description:
    - "returns the 'clone string' for all repositories of all projects that users can read"

author:
    - Oscar Hermosa (osmollo@proton.me)
'''

EXAMPLES = '''
# Get all repositories
- name: "get 1p cli version"
  get_bitbucket_repos:
    host: foo.bar.bitbucket.com
    user: foo
    token: bar
    projects:
        - foo1
        - foo2
        - bar2
  register: get_response

- debug: var=get_response.version
'''

RETURN = '''
version:
    description: All repositories that user can read
    type: list
    returned: always
'''


def get_bitbucket_response(url, user, token):
    if user:
        auth = HTTPBasicAuth(user, token)
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, auth=auth)
    else:
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['values']
    return None


def get_projects(host, user, token):
    bitbucket_url = f"https://{host}/rest/api/1.0/projects"
    response = get_bitbucket_response(bitbucket_url, user, token)
    if response:
        return [x['key'] for x in response]
    return []


def get_project_repos(host, user, token, project):
    output = []
    bitbucket_url = f"https://{host}/rest/api/1.0/projects/{project}/repos"
    response = get_bitbucket_response(bitbucket_url, user, token)
    if response:
        for repo in response:
            for clone in repo['links']['clone']:
                if clone['name'] == 'ssh':
                    output.append({"repo": clone['href']})
    return output


def get_repositories(host, user=None, token=None, projects=[]):
    output = []
    all_projects = get_projects(host, user, token)
    if projects == []:
        projects = all_projects
    for project in projects:
        if project in all_projects:
            output += get_project_repos(host, user, token, project)
    return output


def run_module():
    fields = {
        "host": {
            "required": True,
            "type": "str"
        },
        "user": {
            "required": False,
            "default": None,
            "type": "str"
        },
        "token": {
            "required": True,
            "type": "str",
        },
        "projects": {
            "default": [],
            "type": "list"
        }
    }

    result = dict(
        changed=False,
        repositories=list
    )

    module = AnsibleModule(
        argument_spec=fields,
        supports_check_mode=True
    )

    result['repositories'] = get_repositories(module.params['host'],
                                              module.params['user'],
                                              module.params['token'],
                                              module.params['projects'])
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
