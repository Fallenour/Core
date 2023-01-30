# pull official base image

## Use for Alpine
# FROM python:3.8.2-alpine

## Use for Ubuntu
FROM ubuntu:22.04

## Use for Alpine
#RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
# RUN apk update
#RUN apk add --virtual build-dependencies build-base gcc wget git curl pytest

## Use for Ubuntu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install gcc wget git curl python3-pip python3-pytest -y

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## Use for Alpine
# install dependencies
#RUN pip3 install --upgrade pip
#COPY ./requirements.txt /usr/src/app/requirements.txt
#RUN pip3 install -r requirements.txt

## Use for Ubuntu
# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

# install atomic-red-team
RUN mkdir /home/atomic-red-team && cd /home/atomic-red-team && git clone https://github.com/redcanaryco/atomic-red-team

## Use with Alpine
# install Metasploit
# RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall

## Use with Ubuntu
# install Metasploit
# RUN touch /etc/apt/sources.list.d/metasploit-framework.list
# RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall


# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]