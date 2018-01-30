# Development workflow

**Version:0.1.0**

The development should follow the [github flow](https://guides.github.com/introduction/flow/) which means that features or fixes should be pushed into a separate branch and merged into the master or development branch by creating a pull request.

This allows us to organize code reviews and run automated tests before updating the development/master branch.

## Branches

Pattern for branch names are:

**'refactor/name'**

**'feature/name'**

**'fix/name'**

Feature branches should only be merged into the development branch.
The master branch contains the code of the latest release.

## Releases

The release version names and tags should follow [semantic versioning](http://semver.org/).

### Commit Messages

Commit messages should follow the angular.js convention making it easy to autogenerate release notes using [clog](https://github.com/clog-tool/clog-cli):

https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#commit

***Example Commit Message:***

* feat(gui): created new button

* fix(cli): added missing parameter

## Repository Guides

Each repository should have it's own

* **Short description** of the tool or library

* **User Guide** (How to use the tool or library.)

* **Developer Guide** with a section for
   
   * how to build the tool/library
   
   * the repository structure (e.g.: description of submodules) # Development workflow
