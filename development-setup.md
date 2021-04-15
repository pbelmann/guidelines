# Where to find passwords and files needed for development
We store necessary passwords and files on a CeBiTec volume. To be able to access it, you need an account with CeBiTec, which you have to register at their office.  
Once you have an account with CeBiTec, you will be added to the `denbi-portal-backup` group. Visit [myCeBiTec](https://www.cebitec.uni-bielefeld.de/mycebitec/), log in,
click on `Account` in the `Unix` row and activate the `denbi-portal-backup` tick.  
Now you can create a ssh connection and navigate to the volume:  
```shell script
ssh <your-CeBiTec-login-name>@porta.cebitec.uni-bielefeld.de
cd /vol/denbi_cloud_portal_dev/
```
Here you will find directories for the different repositories. Each contains necessary passwords and files, further details
on how to use them can be found in the respective Github repositories.  
For usage of non-repository files or generally if in doubt, please ask a team member.

# Running the portal locally
To get started with developing, you need to clone the [cloud-api](https://github.com/deNBI/cloud-api), 
the [cloud-portal-webapp](https://github.com/deNBI/cloud-portal-webapp) and (optionally) the [cloud-portal-client](https://github.com/deNBI/cloud-portal-client) repository.  
Use the cloud-portal-client if you are going to work with SimpleVM, i.e. when creating SimpleVM projects or interacting with virtual machines.  
The necessary files and passwords for the api and the client can be found by following the steps above, the guides on how
to start the applications can be found in their respective Github repositories.  

# Short overview of some repositories/components
## cloud-api
The [api](https://github.com/deNBI/cloud-api) is the backend of the portal. It is used to process data, save data and request data from other components.
## cloud-portal-webapp
The [webapp](https://github.com/deNBI/cloud-portal-webapp) is the frontend of the portal. It is used as the User Interface, it gets and sends data to and from the API.
## cloud-portal-client
The [client](https://github.com/deNBI/cloud-portal-client) connects to an Openstack project and is important for interacting with SimpleVM projects and virtual machines. It has to run if you want to:
- Approve SimpleVM projects
- Run/Stop/Check/... virtual machines
- Attach/Detach/... volumes
- Create/Delete/... snapshots
## cloud-portal
The [cloud-portal](https://github.com/deNBI/cloud-portal) repository is used to setup all components automatically on staging and production. Not every component it sets up is listed here, for more information please see the repository.
## OS_project_usage_exporter
The [usage exporter](https://github.com/deNBI/OS_project_usage_exporter) is setup by each compute center individually and harvests usage data, which will be processed by the os_credits component.
## os_credits
The [os credits](https://github.com/deNBI/os_credits) component saves usage data, calculates used credits which are updated in Perun and provides a REST api for different usage cases.
## project_usage
The [project usage repository](https://github.com/deNBI/project_usage) is used to setup the exporter component or the credits component or both on dev, staging and production. Use this if you want to have the complete credits stack running.
## cloud-user-docs
The [user docs repository](https://github.com/deNBI/cloud-user-docs) contains the files our WIKI is build with.
## simpleVMWebGateway
The [simpleVMWebGateway](https://github.com/deNBI/simpleVMWebGateway) component is also known as FORC. It handles the connection to research environments.
## landing_page
The [landing page](https://github.com/deNBI/landing_page) repository contains the needed files for our [Homepage](https://cloud.denbi.de).

# Some useful links
- [Test-Results](https://portal-dev.denbi.de/test-results/)
Results of the last test that ran on the staging
- [Eslint Intellij](https://www.jetbrains.com/help/idea/eslint.html)
Information how to setup Eslint in Intellij
- [Perun](https://perun.elixir-czech.cz)  
Contains information about groups, resources and members.
- [Openstack Bielefeld](https://openstack.cebitec.uni-bielefeld.de)  
Dashboard for openstack projects and our simplevm pool project. E.g. contains virtual machines, volumes and snapshots.
- [Staging](https://portal-dev.denbi.de/)  
- [Local BUG throwing link](http://localhost:8000/api/v0/voManagers/test_bug/?error=0)  
Depending on error number different errors:  
0: raise exception  
1: logger.error  
2: catched exception and logger.exception  
x: error because no response  
- [OIDC Token list](https://login.elixir-czech.org/oidc/)  
Choose links on the left site to manage approved sites and see active OIDC tokens.

