#!/usr/bin/python

from ansible.module_utils.basic import *
import requests
import json

DOCUMENTATION = '''
---
module: github_repo
short_description: Manage your repos on Github
'''

EXAMPLES = '''
- name: Create a github Repo
  github_repo:
    github_auth_key: "..."
    name: "Hello-World"
    description: "This is your first repository"
    private: yes
    has_issues: no
    has_wiki: no
    has_downloads: no
  register: result

- name: Delete that repo
  github_repo:
    github_auth_key: "..."
    name: "Hello-World"
    state: absent
  register: result
'''

api_url = "https://api.github.com"


def github_get_owner(data=None):
    headers = {
        "Authorization": "token {}".format(data['github_auth_key'])
    }
    url = "{}/user/repos".format(api_url)
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        return result.json()[0]["owner"]["login"]
    else:
        return None


def github_repo_present(data):
    api_key = data['github_auth_key']
    del data['state']
    del data['github_auth_key']

    headers = {
        "Authorization": "token {}".format(api_key)
    }
    url = "{}{}".format(api_url, '/user/repos')
    result = requests.post(url, json.dumps(data), headers=headers)

    if result.status_code == 201:
        return False, True, result.json()
    elif result.status_code == 422:
        return False, False, result.json()
    else:
        return True, False, result.json()


def github_repo_absent(data=None):
    headers = {
        "Authorization": "token {}".format(data['github_auth_key'])
    }
    url = "{}/repos/{}/{}".format(api_url, github_get_owner(data), data['name'])
    result = requests.delete(url, headers=headers)

    if result.status_code == 204:
        return False, True, result.json()
    elif result.status_code == 404:
        return False, False, result.json()
    else:
        return True, False, result.json()


def main():

    fields = {
        "github_auth_key": {"required": True, "type": "str"},
        "name": {"required": True, "type": "str"},
        "description": {"required": False, "type": "str"},
        "private": {"default": False, "type": "bool"},
        "has_issues": {"default": True, "type": "bool"},
        "has_wiki": {"default": True, "type": "bool"},
        "has_downloads": {"default": True, "type": "bool"},
        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
    }

    choice_map = {
        "present": github_repo_present,
        "absent": github_repo_absent,
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error", meta=result)


if __name__ == '__main__':
    main()
