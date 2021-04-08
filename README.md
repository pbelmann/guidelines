# Guidelines

This project is organized by using elements of [scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)).
It is based on the five values:

* **Commitment**
* **Focus**
* **Openness**
* **Respect**
* **Courage**

and has three conditions:

* **Transparency**  
Information must be available to everyone
* **Inspection**  
Decide in specific time intervals if the current working method is effective.
* **Adaption**  
If the teams detects methods that can be improved it must do that!

## Meetings

Our Meetings consist of four parts:

* **Sprint Review**  
The developer team first discusses/shows/presents the Issues found in the **Ready for sprint review** column. 
All issues have to work on staging.
The product owner must check which sprint items are done. (99% percent of the task is not done!).
The developer team then continues discussing/showing/presenting the issues and their progress/feasibility from the 
**Release critical**, **In progress**, **Bugs** and **Current sprint** board.
During this phase one team member collects all new issues we discover in the process.
Under certain conditions the product backlog must be adapted. 
  
* **Retrospective**  
In the context of the Retrospective the developer team tries to improve the next sprint based on the experience of 
the last one. For example the team could decide to modify the definition of done. Questions should be asked like:
  * How was the collaboration with others?
  * How can we improve our communication?
  * Do we really need all the development tools? Maybe we can remove or swap out specific tools.
  * How can we build faster and better our product?

* **Sprint planning 1:**  
This part answers the question which product increment should be created in the next sprint.
It is based on the current product backlog, the current development status and the velocity 
and net work time of the team. The product owner presents product backlog for the next sprint.
Just the development team is able to decide which items can be done during the next sprint.
At the end the development team must define a common goal for the next sprint.

* **Sprint planning 2:**  
This part answers how we should approach the tasks. The product owner presents the backlog items which are sorted by
priority. The team develops based on those backlog items tasks which represent the sprint backlog. 
Those tasks should not take more time than one working day. 
The tasks are valued by using story points for estimating the work of the next sprint.
How to evaluate tasks by using story points is described [here](story_points.md).

### Organisation:

The timeboxing principle is used to shorten the length of meetings and to work efficiently. For this purpose, the team jointly sets timeboxes for the meeting and the parts of the meeting described above. A possible allocation would be, for example, 1 hour for the sprint review, 30 minutes for the retrospective and another hour for planning the following sprint.
An important role is taken on by the Scrum Master, who monitors the compliance with the time boxes in the interest of meeting efficiency and ensures that the time boxes are adhered to. If a story is not discussed because there is no time left, it moves to the next meeting. Moreover, it should be ensured that discussions and consultations that do not affect the whole team are held in a small group outside of the regular meetings.  

Further information on Timeboxing can be found [here](https://www.visual-paradigm.com/scrum/what-are-scrum-time-boxed-events/).
  
## Definition of Done
We say a task or issue or sprint item is done if  
* It is reviewed and tested by one of the team members.
* It is documented either in the technical or the user documentation.
* The final result is available on the staging instance.

## Sprint Commissioner
For each sprint there is a sprint commissioner. The role of the sprint commissioner is rotated every sprint.

The tasks of the sprint commissioner are as follows:

* **Second Reviewer**  
The sprint commissioner is always the second reviewer. He/She makes sure all points of the Issue Template are fulfilled.
This includes adjusting the existing e2e tests if necessary.

* **Security Fixes**
The sprint commissioner keeps track of the security scans for all repositories with activated scans and fixes errors and warnings displayed there.
  
* **Staging**  
He/She is responsible for ensuring that the staging instance is up-to-date and online at the sprint meeting.
The official deadline until PRs have to be reviewed and branches have to be merged into the development branch, to get 
into the staging release, is Thursday 16:00 every week. Dev states after this deadline should not be part of the staging release.
  
* **Releasing**  
He/She updates the various changelogs and creates the new releases.
The releases are based on the state of the staging and can be created as soon as the changes on the staging are reviewed in the meeting by all team members and no issues remain in the "Release-Critical"-column of the sprint-board.
  
* **Bugs**  
He/She creates the incoming bug issues in github and is initially responsible for them, but can also forward the issues if needed.
  
* **Dependabot PRs**  
The commissioner reviews pull requests created by dependabot.

**The priority of the Sprint Commissioner is to handle bugs and user requests. This also needs to be taken into account when planning the sprint.**


## Feature Commissioner
For each sprint there is a feature commissioner.  
The role of the feature commissioner is usually taken over by the person who was the sprint commissioner in the previous sprint.

The Commissioner has the following responsibilities:

* **Listing new features**  
The commissioner reviews the features of the new releases that have been released in his sprint.
He lists the new features and user-relevant changes and saves them together with a short description in a draft within WordPress.

* **Writing a post**  
If a new post is to be created in the course of the sprint, the commissioner summarizes the points in the respective changelogs into a short text so that it can be published. The publication is tracked via WordPress. In the course of this a new draft get's created in WordPress , so that the commissioner of the following sprint can start with an empty draft. 


## Development Workflow

See the [development workflow](development-workflow.md).
