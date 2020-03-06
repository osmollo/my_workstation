#!/usr/bin/python

from ansible.module_utils.basic import *
import requests
import json

DOCUMENTATION = '''
---
module: gitlab_get_forks
short_description: Manage your repos on gitlab
'''

EXAMPLES = '''
- name: get forks of gitlab repository
  gitlab_get_forks:
    gitlab_auth_key: "..."
    name: "test_repository"
  register: result

- name: get forked repositories
  debug: var=result.forks
'''

api_url = "https://gitlab.com/api/v4"


def gitlab_get_user_id(data=None):
    headers = {
        "PRIVATE-TOKEN": "{}" . format(data['gitlab_auth_key'])
    }
    url = "{}/user" . format(api_url)
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        return result.json()["username"]
    else:
        return None


def gitlab_get_project_id(data=None):
    headers = {
        "PRIVATE-TOKEN": "{}" . format(data['gitlab_auth_key'])
    }
    url = "{}/users/{}/projects?pagination=keyset&per_page=99&order_by=id" . format(api_url, gitlab_get_user_id(data))
    result = requests.get(url, headers=headers)

    if result.status_code == 200:
        for i in result.json():
            if i["name"] == data["name"]:
                return i["id"]
        return None
    else:
        return None


def get_forks(token, repository):
    data = {
        "gitlab_auth_key": token,
        "name": repository
    }

    headers = {
        "PRIVATE-TOKEN": "{}" . format(token)
    }
    url = "{}/projects/{}/forks" . format(api_url, gitlab_get_project_id(data))
    result = requests.get(url, headers=headers)

    list = []
    if result.status_code == 200:
        for fork in result.json():
            list.append({
                        "user": fork["owner"]["username"],
                        "remote": "git@gitlab.com:{}/{}.git".format(fork["owner"]["username"], repository)
                    })
        return list
    else:
        return []


    if result.status_code == 202:
        return False, True, {"status": "SUCCESS"}
    if result.status_code == 404:
        result = {"status": result.status_code, "data": result.json()}
        return False, False, result
    else:
        result = {"status": result.status_code, "data": result.json()}
        return True, False, result


def main():
    module_args = dict(
        gitlab_auth_key=dict(type='str', required=True),
        name=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        forks=list
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result['forks'] = get_forks(token=module.params["gitlab_auth_key"],
                                repository=module.params["name"])
    module.exit_json(**result)


if __name__ == '__main__':
    main()
