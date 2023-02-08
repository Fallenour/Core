##################################################################################################
#                                           Docker                                               #
##################################################################################################

##### Information Commands ###


## To Show all ips and name in the new docker ##
# Source: https://gist.github.com/ipedrazas/2c93f6e74737d1f8a791
sudo docker ps -q | sudo xargs -n 1 docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} {{ .Name }}' | sudo  sed 's/ \// /'


## Get ports connecting to and from the containers to host, name of hosts, when created, etc ##

sudo docker ps



##### Web Troubleshooting Commands ###


### Building the Container

sudo docker-compose up -d --build ### General Build

sudo docker-compose up -d --build --scale celery=3 ### Build with 3 celery workers instead of 1.


# Sources #
https://github.com/testdrivenio/django-on-docker
https://github.com/testdrivenio/fastapi-crud-async
https://ably.com/blog/no-we-dont-use-kubernetes