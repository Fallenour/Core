##################################################################################################
#                                           Docker                                               #
##################################################################################################
##### Web Troubleshooting Commands ###


### Building the Container

sudo docker-compose up -d --build ### General Build

sudo docker-compose up -d --build --scale celery=3 ### Build with 3 celery workers instead of 1.

# Sources #
https://github.com/testdrivenio/django-on-docker
https://github.com/testdrivenio/fastapi-crud-async
https://ably.com/blog/no-we-dont-use-kubernetes