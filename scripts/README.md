# Github Scripts

There are several scripts available for github that automate the creation, closing and moving of issue cards.

The existing scripts perform the following tasks:

* Closing all issues which are in the "Done" column from the "Weekly Sprint" project  *[close_done_issues.py]*

* Create Issues and Cards from a google spreadsheet. *[create_issue_and_cards.py]*

* Move all cards from "Ready for Sprint Review" to "Done". *[move_review_to_done.py]*

* Set all Public Keys from the portal-dev Team to authorized_keys* *[set_portal_dev_team_keys.py]*

## Preparation
To use the scripts you need to install several modules.

~~~BASH
	pip3 install -r requirements.txt
~~~


You also need a "credentials.json" in the scripts folder, which gives you access to the google spreadsheet. 
  


## Running the Scripts

You can run the scripts directly with:

~~~BASH
	python3 close_done_issues.py REPO_SCOPED_TOKEN
	python3 create_issue_and_cardy.py REPO_SCOPED_TOKEN
	python3 move_review_to_done.py REPO_SCOPED_TOKEN
	python3 set_portal_dev_team_keys.py ORG_READ_SCOPED_TOKEN [-replace]
~~~

