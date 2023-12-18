#!/usr/bin/python

import os.path
import operator
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
    git_directory: /foo/bar/git
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


def get_project_repos(host, user, token, project, git_directory):
    output = []
    bitbucket_url = f"https://{host}/rest/api/1.0/projects/{project}/repos/?limit=5000"
    response = get_bitbucket_response(bitbucket_url, user, token)
    if response:
        for repo in response:
            for clone in repo['links']['clone']:
                if clone['name'] == 'ssh':
                    output.append({
                        "repo": clone['href'],
                        "dest": os.path.join(git_directory,
                                             clone['href'].split('/')[-1].split('.')[0])
                    })
    return output


def process_duplicates(list_of_repos):
    temp = [os.path.basename(x['dest']) for x in list_of_repos]
    for i in range(len(list_of_repos)):
        basename = os.path.basename(list_of_repos[i]['dest'])
        if operator.countOf(temp, basename) > 1:
            project = list_of_repos[i]['repo'].split('/')[3]
            list_of_repos[i]['dest'] = list_of_repos[i]['dest'].replace(basename,
                                                                        f'{project}_{basename}')
    return list_of_repos


def get_repositories(host, user=None, token=None, projects=[], git_directory=None):
    output = []
    tmp = {}
    all_projects = get_projects(host, user, token)
    if projects == []:
        projects = all_projects
    for project in projects:
        if project in all_projects:
            output += get_project_repos(host, user, token, project, git_directory)
    return process_duplicates(output)


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
        },
        "git_directory": {
            "required": True,
            "type": "str"
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
                                              module.params['projects'],
                                              module.params['git_directory'])
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
