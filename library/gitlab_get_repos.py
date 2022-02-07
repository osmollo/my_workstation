#!/usr/bin/python

from ansible.module_utils.basic import *
import requests
import json

DOCUMENTATION = '''
---
module: gitlab_get_repos
short_description: Manage your repos on gitlab
'''

EXAMPLES = '''
- name: get repos of gitlab repository
  gitlab_get_repos:
    gitlab_auth_key: "..."
  register: result

- name: get forked repositories
  debug: var=result.repos
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


def get_repos(token):
    data = {
        "gitlab_auth_key": token
    }

    headers = {
        "PRIVATE-TOKEN": "{}".format(token)
    }
    who_am_i = gitlab_get_user_id(data)
    url = "{}/users/{}/projects?pagination=keyset&per_page=99&order_by=id".format(api_url, who_am_i)
    result = requests.get(url, headers=headers)

    list = []
    if result.status_code == 200:
        for repo in result.json():
            list.append({
                        "repo": repo["name"],
                        "repo_url": "git@gitlab.com:{}/{}.git".format(who_am_i, repo["name"])
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
        gitlab_auth_key=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        repos=list
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result['repos'] = get_repos(token=module.params["gitlab_auth_key"])
    module.exit_json(**result)


if __name__ == '__main__':
    main()
