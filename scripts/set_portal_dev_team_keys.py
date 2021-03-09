#!/usr/bin/env python3
import os
import sys

import requests

ORG = "deNBI"
TEAM = "portal-dev"
AUTHORIZED_KEYS = "~/.ssh/authorized_keys"

try:
    ACCESS_TOKEN = sys.argv[1]
    HEADERS = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer " + ACCESS_TOKEN}
except:
    print("The first param should be your access_token")
    sys.exit(1)


def check_for_errors(resp, *args, **kwargs):
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        print(e)
        print(f"Request failed! Content:{resp.content} ")


def get_team_members():
    print(f"Getting Team Members {ORG}:{TEAM}")
    headers = HEADERS
    url = f"https://api.github.com/orgs/{ORG}/teams/{TEAM}/members"
    r = requests.get(
        url=url,
        headers=headers,
        hooks={"response": check_for_errors},

    )
    return [entry["login"] for entry in r.json()]


def get_ssh_keys_user(user):
    print(f"Getting SSH Keys {user}")
    url = f"https://github.com/{user}.keys"
    r = requests.get(url=url)
    return r.text


def append_keys_to_authorized_keys(key):
    with open(AUTHORIZED_KEYS, "a") as key_file:
        key_file.write(key)
        key_file.write("\n")

        print(f"Added Key [{key}] to authorized keys!")


keys = []
for member in get_team_members():
    for key in get_ssh_keys_user(member).split("\n"):
        if key:
            key = f"{key} {member}\n"
            keys.append(key)

if len(keys) > 0:
    if len(sys.argv) == 3 and sys.argv[2] == "-replace":
        print("Remove old authorized keys file")
        os.remove(AUTHORIZED_KEYS)
    for key in keys:
        append_keys_to_authorized_keys(key)
