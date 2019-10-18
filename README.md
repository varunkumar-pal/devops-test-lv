# devops-test-lv
# Thw following files have been added for the Docker Challenge:

Docker.zip
which contains
Dockerfile - within which the following tasks are performed
1. use tomcat as the base image (could use the :latest tag to use the latest version)
2. make sure to run it as a root user
3. copy the custom tomcat-users.xml which contains the admin credentials
4. copy the context.xml which has /pebble as the context
5. download the pebble.war after creating a temp location using curl
6. copy the war file in the webapss folder to deploy the war file
7. make sure tomcat starts at 8080
8. start catalina service to ensure that the war is deployed properly

The other files that are contained in the zip are 
tomcat-users.xml and context.xml file


### Automation Challenge:

The solution contains the following files:

playbook.yml - used by Ansible 
automation.spec - SPEC file for rpm

Following steps have been automated by playbook.yml
1. Install rpmbuild that is needed
2. copy automation.tar.gz to the SOURCES directory
3. copy automation.spec to SPECS directory
4. build the rpm file
5. Verify the build
6. install the rpm file
7. verify the installation
