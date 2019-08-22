# Github Scripts

There are several scripts available for github that automate the creation, closing and moving of issue cards.

The existing scripts perform the following tasks:

* Closing all isues which are in the "Done" column from the "Weekly Sprint" project.

* Create Issues and Cards from a google spreadsheet.

* Move all cards from "Ready for Sprint Review" to "Done".

## Preparation
To use the script you need to install several modules.

~~~BASH
	pip3 install -r requirements.txt
~~~
  or
~~~BASH
	make requirements
~~~

You also need a "credentials.json" in the scripts folder, which gives you access to the google spreadsheet. 
  


## Running the Scripts

You can run the scripts directly with (python3 shebang is used):

~~~BASH
	./close_done_issues.py
	./create_issue_and_cardy.py
	./move_review_to_done.py
~~~

Or using the make commands:

~~~BASH
	make move_review_to_done
	make create_issues_and_cards
	make close_done_cards
~~~
