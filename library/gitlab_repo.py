#!/usr/bin/python

from ansible.module_utils.basic import *
import requests
import json

DOCUMENTATION = '''
---
module: gitlab_repo
short_description: Manage your repos on gitlab
'''

EXAMPLES = '''
- name: Create a gitlab Repo
  gitlab_repo:
    gitlab_auth_key: "..."
    name: "Hello-World"
    description: "This is your first repository"
    private: yes
    has_issues: no
    has_wiki: no
    has_downloads: no
  register: result

- name: Delete that repo
  gitlab_repo:
    gitlab_auth_key: "..."
    name: "Hello-World"
    state: absent
  register: result
'''

api_url = "https://gitlab.com/api/v4"


def gitlab_get_user_id(data=None):
    headers = {
        "PRIVATE-TOKEN": "{}".format(data['gitlab_auth_key'])
    }
    url = "{}/user".format(api_url)
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        return result.json()["username"]
    else:
        return None


def gitlab_get_project_id(data=None):
    headers = {
        "PRIVATE-TOKEN": "{}".format(data['gitlab_auth_key'])
    }
    url = "{}/users/{}/projects?pagination=keyset&per_page=99&order_by=id".format(api_url, gitlab_get_user_id(data))
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        for i in result.json():
            if i["name"] == data["name"]:
                return i["id"]
        return None
    else:
        return None


def gitlab_repo_present(data):
    if gitlab_get_project_id(data):
        return False, False, {"status": "Repository already exists"}
    else:
        headers = {
            "PRIVATE-TOKEN": "{}".format(data['gitlab_auth_key'])
        }
        url = "{}{}".format(api_url, '/projects')
        result = requests.post(url, data=data, headers=headers)

        if result.status_code == 201:
            return False, True, result.json()
        else:
            return True, False, result.json()


def gitlab_repo_absent(data=None):
    if gitlab_get_project_id(data):
        headers = {
            "PRIVATE-TOKEN": "{}".format(data['gitlab_auth_key'])
        }
        url = "{}/projects/{}".format(api_url, gitlab_get_project_id(data))
        result = requests.delete(url, headers=headers)

        if result.status_code == 202:
            return False, True, result.json()
        else:
            return True, False, result.json()
    else:
        return False, False, {"status": "Repository doesn't exist"}


def main():

    fields = {
        "gitlab_auth_key": {"required": True, "type": "str"},
        "name": {"required": True, "type": "str"},
        "description": {"required": False, "type": "str"},
        "visibility": {"default": "private", "type": "str"},
        "issues_enabled": {"default": True, "type": "bool"},
        "wiki_enabled": {"default": True, "type": "bool"},
        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
    }

    choice_map = {
        "present": gitlab_repo_present,
        "absent": gitlab_repo_absent,
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error", meta=result)


if __name__ == '__main__':
    main()
