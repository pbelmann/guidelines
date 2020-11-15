#!/usr/bin/env python3

import sys

import requests

DONE_COLUMN = "Done"
READY_FOR_REVIEW_COLUMN = "Ready for Sprint Review"
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

    )
    cards = r.json()
    while "next" in r.links:
        print("Next Page: {}".format(r.links["next"]["url"]))
        r = requests.get(
            url=r.links["next"]["url"],
            headers=headers,

        )
        cards.extend(r.json())

    return cards


def move_card_to_column(card, column):
    params = {"column_id": column["id"], "position": "top"}
    url = "https://api.github.com/projects/columns/cards/{}/moves".format(card["id"])
    headers = {"Accept": "application/vnd.github.v3+json application/vnd.github.inertia-preview+json"}
    r = requests.post(
        url=url,
        headers=headers,
        json=params

    )
    print("Moved Card {}".format(card["id"]))
    return r.json()


def close_issue(issue_url):
    params = {"state": "closed"}
    headers = HEADERS
    r = requests.patch(
        url=issue_url,
        headers=headers,
        json=params

    )
    print("Closed Issue {}".format(issue_url))
    return r.json()


def move_cards_to_column(cards, column):
    for card in cards:
        close_issue(card["content_url"])
        move_card_to_column(card, column)


if __name__ == "__main__":

    projects = get_organisation_projects()
    weekly_project = filter_projects(filter_name=WEEKLY_SPRINT_PROJECT, projects=projects)
    columns = get_project_columns(weekly_project)
    ready_for_review_column = get_specific_column(filter_name=READY_FOR_REVIEW_COLUMN, columns=columns)
    done_column = get_specific_column(filter_name=DONE_COLUMN, columns=columns)
    ready_for_review_cards = get_cards_by_columns(column=ready_for_review_column)
    move_cards_to_column(cards=ready_for_review_cards, column=done_column)
