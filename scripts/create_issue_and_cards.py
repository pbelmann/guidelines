#!/usr/bin/env python3

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import getpass

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1xfiYlW0Icpvu0-ERY55cjpMsJW-YwS5gHBlrivHPNtE'
SAMPLE_RANGE_NAME = 'A2:G'
HEADERS = {
    "Accept": "application/vnd.github.v3+json application/vnd.github.inertia-preview+json application/vnd.github.symmetria-preview+json"}
OWNER = "deNBI"
WEEKLY_SPRINT_PROJECT = "Weekly Sprint"
ISSUES_DICT = {}


class IssueCard:
    def __init__(self, title, description, repository, labels, project, column):
        self.title = title
        self.description = description
        self.repository = repository
        self.labels = labels
        self.project = project
        self.column = column

    def __str__(self):
        return "{}:{}".format(self.title, self.description)

    __repr__ = __str__


def check_if_issue_exist_in_repository(issue):
    global ISSUES_DICT
    try:
        if issue.repository not in ISSUES_DICT:
            rep_issues = get_issues_by_repository(repository=issue.repository)
        else:
            rep_issues = ISSUES_DICT[issue.repository]
        for rep_issue in rep_issues:
            if issue.title == rep_issue["title"]:
                print("Issue {} already exists".format(issue))
                return True
        return False
    except Exception as ex:

        print("Error produced with issue {} \n error {}".format(issue, ex))
        return True


def get_issues_by_repository(repository):
    url = "https://api.github.com/repos/{}/{}/issues".format(OWNER, repository)
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        auth=(USER_NAME, PASSWORD),

    )
    issues = r.json()
    while "next" in r.links:
        print("\tNext Page: {}".format(r.links["next"]["url"]))
        r = requests.get(
            url=r.links["next"]["url"],
            headers=headers,
            auth=(USER_NAME, PASSWORD),

        )
        issues.extend(r.json())
    ISSUES_DICT.update({repository: issues})
    return issues


def get_cards_by_columns(column):
    url = "https://api.github.com/projects/columns/{}/cards".format(column["id"])
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        auth=(USER_NAME, PASSWORD),

    )
    cards = r.json()
    while "next" in r.links:
        print("Next Page: {}".format(r.links["next"]["url"]))
        r = requests.get(
            url=r.links["next"]["url"],
            headers=headers,
            auth=(USER_NAME, PASSWORD),

        )
        cards.extend(r.json())

    return cards


def create_issue(issue):
    params = {"title": issue.title, "body": issue.description}
    url = "https://api.github.com/repos/{}/{}/issues".format(OWNER, issue.repository)
    headers = HEADERS
    r = requests.post(
        url=url,
        headers=headers,
        auth=(USER_NAME, PASSWORD),
        json=params

    )
    vals = r.json()
    issue.number = vals["number"]
    issue.id = vals["id"]
    print("Created Issue: {}".format(issue))
    return issue


def add_label_to_issue(labels, issue):
    params = {"labels": labels}
    url = "https://api.github.com/repos/{}/{}/issues/{}/labels".format(OWNER, issue.repository, issue.number)
    headers = HEADERS
    r = requests.post(
        url=url,
        headers=headers,
        auth=(USER_NAME, PASSWORD),
        json=params

    )
    return r.json()


def get_project_columns(project):
    url = "https://api.github.com/projects/{}/columns".format(project["id"])
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        auth=(USER_NAME, PASSWORD),

    )
    return r.json()


def get_specific_column(filter_name, columns):
    for column in columns:
        if filter_name == column['name']:
            return column
    return None


def get_organisation_projects():
    url = "https://api.github.com/orgs/deNBI/projects"
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        auth=(USER_NAME, PASSWORD),

    )
    return r.json()


def filter_projects(filter_name, projects):
    for project in projects:
        if filter_name == project['name']:
            return project
    return None


def create_card_for_issue(issue, column):
    params = {"content_id": issue.id, "content_type": "Issue"}
    url = "https://api.github.com/projects/columns/{}/cards".format(column["id"])
    headers = HEADERS
    r = requests.post(
        url=url,
        headers=headers,
        auth=(USER_NAME, PASSWORD),
        json=params

    )
    return issue


def values_to_issue_cards(values):
    issue_cards = []
    for row in values:
        new_issue_card = IssueCard(title=row[0], description=row[1], repository=row[2], labels=row[3].split(" "),
                                   project=row[4],
                                   column=row[5])
        issue_cards.append(new_issue_card)
    return issue_cards


def create_issues_and_cards(issue_cards):
    for issue in issue_cards:
        issue_card_column = get_specific_column(filter_name=issue.column, columns=COLUMNS)
        if not check_if_issue_exist_in_repository(issue=issue):
            issue = create_issue(issue)
            add_label_to_issue(labels=issue.labels, issue=issue)
            create_card_for_issue(issue=issue, column=issue_card_column)


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        issue_cards = values_to_issue_cards(values=values)
        create_issues_and_cards(issue_cards=issue_cards)


if __name__ == '__main__':
    print("Enter username:")
    USER_NAME = input()
    print("Enter password:")
    PASSWORD = getpass.getpass()
    projects = get_organisation_projects()
    weekly_project = filter_projects(filter_name=WEEKLY_SPRINT_PROJECT, projects=projects)
    COLUMNS = get_project_columns(weekly_project)
    main()
