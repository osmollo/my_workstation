#!/usr/bin/env python3

import os
import requests

github_api = "https://api.github.com"
github_token = os.environ['GITHUB_TOKEN']
owner = os.environ['GITLAB_USER_LOGIN']
repo = os.environ['CI_PROJECT_NAME']
headers = {
    "Accept": "application/vnd.github.v3+json"
    }


def get_text_from_markdown():
    pass


def create_github_release():
    url = "{}/repos/{}/{}/releases".format(github_token, owner, repo)
    tag = get_tag()
    data = {
        "tag_name": tag,
        "body": get_text_from_markdown(),
        "name": tag
        }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == "201":
        return True
    else:
        return False


def get_tag():
    pass


def get_github_token():
    pass


if __name__ == "__main__":
    pass
