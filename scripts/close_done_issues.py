#!/usr/bin/env python3

import sys

import requests

DONE_COLUMN = "Done"
WEEKLY_SPRINT_PROJECT = "Weekly Sprint"
try:
    ACCESS_TOKEN = sys.argv[1]
    HEADERS = {
        "Accept": "application/vnd.github.v3+json application/vnd.github.inertia-preview+json application/vnd.github.symmetria-preview+json",
        "Authorization": "Bearer " + ACCESS_TOKEN}
except:
    print("The first param should be your access_token")
    sys.exit(1)

def check_for_errors(resp, *args, **kwargs):
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        print("Request failed! Please Check if u use the right token!")
        sys.exit(1)


def get_organisation_projects():
    url = "https://api.github.com/orgs/deNBI/projects"
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        hooks={"response": check_for_errors},

    )
    return r.json()


def filter_projects(filter_name, projects):
    for project in projects:
        if filter_name == project['name']:
            return project
    return None


def get_project_columns(project):
    url = "https://api.github.com/projects/{}/columns".format(project["id"])
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        hooks={"response": check_for_errors},

    )
    return r.json()


def get_specific_column(filter_name, columns):
    for column in columns:
        if filter_name == column['name']:
            return column
    return None


def get_cards_by_columns(column):
    url = "https://api.github.com/projects/columns/{}/cards".format(column["id"])
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        hooks={"response": check_for_errors},

    )
    cards = r.json()
    while "next" in r.links:
        print("Next Page: {}".format(r.links["next"]["url"]))
        r = requests.get(
            url=r.links["next"]["url"],
            headers=headers,
            hooks={"response": check_for_errors},

        )
        cards.extend(r.json())

    return cards


def close_issue(issue_url):
    params = {"state": "closed"}
    headers = HEADERS
    r = requests.patch(
        url=issue_url,
        headers=headers,
        json=params,
        hooks={"response": check_for_errors},

    )
    print("Closed Issue {}".format(issue_url))
    return r.json()


def close_issues(cards):
    print("{} Cards".format(len(cards)))
    for card in cards:
        try:
            close_issue(card["content_url"])
        except Exception as ex:
            print("Could not close Issue from card {} \n\t{}".format(card, ex))
            continue


if __name__ == "__main__":

    projects = get_organisation_projects()
    weekly_project = filter_projects(filter_name=WEEKLY_SPRINT_PROJECT, projects=projects)
    columns = get_project_columns(weekly_project)
    done_column = get_specific_column(filter_name=DONE_COLUMN, columns=columns)
    done_cards = get_cards_by_columns(column=done_column)
    close_issues(cards=done_cards)
