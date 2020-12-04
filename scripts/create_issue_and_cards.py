#!/usr/bin/env python3

from __future__ import print_function

import os.path
import pickle
import sys

import requests
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1xfiYlW0Icpvu0-ERY55cjpMsJW-YwS5gHBlrivHPNtE'
SAMPLE_RANGE_NAME = 'A2:G'

try:
    ACCESS_TOKEN = sys.argv[1]
    HEADERS = {
        "Accept": "application/vnd.github.v3+json application/vnd.github.inertia-preview+json application/vnd.github.symmetria-preview+json",
        "Authorization": "Bearer " + ACCESS_TOKEN}
except:
    print("The first param should be your access_token")
    sys.exit(1)

OWNER = "deNBI"
WEEKLY_SPRINT_PROJECT = "Weekly Sprint"
DEFAULT_SPECIFIC_PROEJCT_COLUMN = "To do"


def check_for_errors(resp, *args, **kwargs):
    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        print(e)
        print(f"Request failed! Content:{resp.content} ")
    # sys.exit(1)


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
    try:
        rep_issues = get_issues_by_repository(repository=issue.repository)

        for rep_issue in rep_issues:
            if issue.title == rep_issue["title"]:
                print("Issue {} already exists".format(issue))
                return True
        return False
    except Exception as ex:

        print("Error produced with issue {} \n error {}".format(issue, ex))
        return True


def get_issues_by_repository(repository):
    print(f"rep: {repository}")
    url = "https://api.github.com/repos/{}/{}/issues".format(OWNER, repository)
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        hooks={"response": check_for_errors},

    )
    issues = r.json()
    while "next" in r.links:
        print("\tNext Page: {}".format(r.links["next"]["url"]))
        r = requests.get(
            url=r.links["next"]["url"],
            headers=headers,
            hooks={"response": check_for_errors},

        )
        issues.extend(r.json())
    return issues


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


def create_issue(issue):
    params = {"title": issue.title, "body": issue.description}
    url = "https://api.github.com/repos/{}/{}/issues".format(OWNER, issue.repository)
    headers = HEADERS
    r = requests.post(
        url=url,
        headers=headers,
        json=params,
        hooks={"response": check_for_errors},

    )
    vals = r.json()
    issue.number = vals["number"]
    issue.id = vals["id"]
    print("Created Issue:\n\tTitle:{0.title}:\n\t\tDescription:{0.description}".format(issue))
    return issue


def add_label_to_issue(labels, issue):
    params = {"labels": labels}
    url = "https://api.github.com/repos/{}/{}/issues/{}/labels".format(OWNER, issue.repository,
                                                                       issue.number)
    headers = HEADERS
    r = requests.post(
        url=url,
        headers=headers,
        json=params,
        hooks={"response": check_for_errors},

    )
    return r.json()


def get_project_columns(project):
    project_name = project["name"]
    print(f"Get columns from organisation {project_name}")

    url = "https://api.github.com/projects/{}/columns".format(project["id"])
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        hooks={"response": check_for_errors},

    )
    columns = r.json()
    columns_names = [c["name"] for c in columns]
    print(f"Found columns from organisation {columns_names}")

    return columns


def get_specific_column(filter_name, columns):
    for column in columns:
        if filter_name == column['name']:
            return column
    return None


def get_organisation_projects():
    print(f"Get projects from organisation deNBI")

    url = "https://api.github.com/orgs/deNBI/projects"
    headers = HEADERS
    r = requests.get(
        url=url,
        headers=headers,
        hooks={"response": check_for_errors},

    )
    return r.json()


def filter_projects(filter_name, projects):
    project_names = [pr["name"] for pr in projects]
    print(f"Searching for {filter_name} project  in {project_names}")

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
        json=params,
        hooks={"response": check_for_errors},

    )

    return issue


def values_to_issue_cards(values):
    issue_cards = []
    for idx,row in enumerate(values):
        if row[0] and row[1] and row[2] and row[3] and row[4]:
            new_issue_card = IssueCard(title=row[0], description=row[1], repository=row[2],
                                       labels=row[3].split(" "),
                                       project=WEEKLY_SPRINT_PROJECT,
                                       column=row[4])
            issue_cards.append(new_issue_card)
        else:
            print(f"Spreadsheet row {idx} is missing some entrys!")
    return issue_cards


def create_issues_and_cards(issue_cards):
    for issue in issue_cards:
        issue_card_column = get_specific_column(filter_name=issue.column, columns=COLUMNS)

        if not check_if_issue_exist_in_repository(issue=issue):
            issue = create_issue(issue)
            if issue.labels:
                add_label_to_issue(labels=issue.labels, issue=issue)
            create_card_for_issue(issue=issue, column=issue_card_column)


def read_issues_from_spreadsheet():
    """Shows basic usage of the Sheets API.
   Prints values from a sample spreadsheet.
   """

    print("Get Issues from spreadsheet")

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
    print(f"Got {len(values)} issues")

    return values


def spreadsheet_issues_to_card_issues(issues):
    print("Start creating issues")

    issue_cards = values_to_issue_cards(values=issues)
    create_issues_and_cards(issue_cards=issue_cards)


if __name__ == '__main__':
    spreadsheet_issues = read_issues_from_spreadsheet()
    projects = get_organisation_projects()
    weekly_project = filter_projects(filter_name=WEEKLY_SPRINT_PROJECT, projects=projects)
    COLUMNS = get_project_columns(weekly_project)
    spreadsheet_issues_to_card_issues(spreadsheet_issues)
