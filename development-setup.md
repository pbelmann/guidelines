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

## Running the portal locally
To get started with developing, you need to clone the [cloud-api](https://github.com/deNBI/cloud-api), 
the [cloud-portal-webapp](https://github.com/deNBI/cloud-portal-webapp) and (optionally) the [cloud-portal-client](https://github.com/deNBI/cloud-portal-client) repository.
The necessary files and passwords for the api and the client can be found by following the steps above, the guides on how
to start the applications can be found in their respective Github repositories.  
