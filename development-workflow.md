# Development workflow

The development should follow the [github flow](https://guides.github.com/introduction/flow/) which means that features or fixes should be pushed into a separate branch and merged into the development, staging or master branch by creating a pull request.  
One must not push directly into dev, staging or master.  
This allows us to organize code reviews and run automated tests before updating the development/staging/master branch.

## On branches
We maintain three separate branches:  
- dev: The **development** branch. Used for new features, refactors and small bug fixes.
- staging: The **staging** branch. Used for maintaining a sprint review ready version of our code and to test critical bug fixes. This branch should be ready the day before the sprint review.
- master: The **production** branch. Used for maintaining production ready code and the latest release. Code in this state should run as smoothly as possible and has to be tested already.

Merging is only allowed in the following direction dev -> staging -> master. Merging in the other directions should ideally not happen.

Pattern for new branch names are:
- **'refactor/name'**  
Should only be merged into the **development** branch.
- **'feature/name'**  
Should only be merged into the **development** branch.
- **'fix/name'**  
Should be merged depending on its importance:  
Minor bug fixes should only be merged into the **development** branch.  
Critical bug fixes should be merged into the **staging** and the **development** branch, i.e. ideally it goes:
fix/bigBug into staging, fix/bigBug into dev, staging into master.

## On commit messages
Commit messages should follow the angular.js convention making it easy to autogenerate release notes using [clog](https://github.com/clog-tool/clog-cli):

https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits

***Example Commit Message:***

* feat(gui): created new button

* fix(cli): added missing parameter

## On pull requests
Merging branches should only happen with a pull request (PR).  
One should assign two reviewers to a PR: the first reviewer tests the code and the second reviewer checks the bullet points in the description.  
In the PR description we address the first and main reviewer with @NameOfFirstReviewer followed by a short description of what should be reviewed and/or what has changed.
If the reviewer has to adjust some settings or has to follow some specific commands, this should be mentioned here.  
The description is followed by automatically generated bullet points, which should be checked by the second reviewer and the PR creator.  
Additionally, every PR will be checked by repository-depended [Github actions](https://docs.github.com/en/actions). Depending on the target branch, you will have to wait until these checks have passed before being able to merge.

## On releases
The release version names and tags should follow [semantic versioning](http://semver.org/) for all releases except of the cloud-portal-webapp. The release version names and tags of should follow [calender versioning](https://calver.org) (known from e.g. Ubuntu). 

## On repositories
Each repository should have its own

* **Short description** of the tool or library  
* **User Guide** (How to use the tool or library.)  
* **Developer Guide** with a section for
   * how to build the tool/library
   * the repository structure (e.g.: description of submodules) # Development workflow


## On the weekly sprint kanban board
We divide our tasks into multiple columns:
- **To do**  
This is equivalent to a Backlog of issues. Every issue that is not part of the ongoing sprint or is not a candidate for the next sprint is collected here.
- **Next sprint candidates**  
Issues in here are suggestions for the next sprint and only live here for a short time. If they are not planned for the next sprint, they move into **To do**.
- **Current sprint**  
Issues that should be worked on and be done in the current sprint live here. If one starts working on them, they should be moved into **In progress**.
- **Bugs**  
Known bugs are collected here and should be labeled with **Bug**. 
Bugs that occur during the sprint and are not known beforehand are labeld **Post-meeting**. 
Bugs that are critical should be additionally labeled with **Critical**. 
If on starts working on them, they should be moved into **In progress**.
- **In progress**  
Issues which have a team member working on them are moved here and should have the respective member assigned.
- **Release critical**  
Reviewed issues from **Ready for sprint review** which are found to be not done, incomplete or buggy but are necessary for the upcoming release are moved here.
- **Ready for sprint review**  
Issues that are working on the staging (or have been completed otherwise if they are a non-code issue), should be moved here so that we may discuss it during sprint review.
- **Done**  
Once an issue has hit our definition of done (see README.md), it should be closed and moved here. Items in this column can be deleted if the column gets too full.


## On the Cloud-Portal repository
We also release the Cloud-Portal repository. When merging staging into master, release the new version with a description of the changes.
This includes changes to environment variables, settings and ansible tags and variables.
