##################################################################################################
#                                           Docker                                               #
##################################################################################################

##### Information Commands ###


## To Show all ips and name in the new docker ##
# Source: https://gist.github.com/ipedrazas/2c93f6e74737d1f8a791
sudo docker ps -q | sudo xargs -n 1 docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} {{ .Name }}' | sudo  sed 's/ \// /'


## Get ports connecting to and from the containers to host, name of hosts, when created, etc ##

sudo docker ps

## Destroy a specific container ##

sudo docker rm <containername>

## Start/Stop a container ##

sudo docker start/stop <containername>

##### Web Troubleshooting Commands ###


### Building the Container

sudo docker-compose up -d --build ### General Build

sudo docker-compose up -d --build --scale celery=3 ### Build with 3 celery workers instead of 1.



### Various Notes, Sort Later ###

# Source: https://www.techsupportpk.com/2022/02/set-up-highly-available-postgresql-cluster-docker-ubuntu.html

sudo docker run -it --name postgres_release12 -e DEBIAN_FRONTEND=noninteractive ubuntu:20.04
sudo docker run -it --name postgres_release12
sudo docker commit postgres_release12 postgres15_ha_image
docker create -it --network pg_network --ip 172.20.0.12 -h postgres3 --name postgres3 postgres15_ha_image
sudo docker network create -d bridge --subnet=172.20.0.0/16 pg_network

192.168.240.3 docker_micro_1
192.168.240.6 docker_celery_1
192.168.240.5 docker_celery-beat_1
192.168.240.4 docker_web_1
192.168.240.2 docker_redis_1

172.20.0.10    postgres1
172.20.0.11    postgres2
172.20.0.12    postgres3


pg1: 10.80.80.195 and pg2: 10.80.80.196

etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380   --listen-peer-urls http://172.20.0.10:2380   --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:2379   --advertise-client-urls http://172.20.0.10:2379   --initial-cluster-token etcd-cluster-1   --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=172.20.0.12   --initial-cluster-state new

postgres1 - 549530025adae0b18a0cd83c9eebd511e5df561b9d066d5aa9d51b19336aea3a
postgres2 - 35691a603696390ce48529924d7d2e3dea727225f8840a884b3576709bf37f27
postgres3 - ef07dcc9ac40e9681ba3fac0aabbe7fe1f6901b3c608f803bfceebe7eb6531c9

micro - 720544d735bad55679c17c0e9dcd0acb53eb0f0d141c9825eaeb2d002de6b40b
citadel - 4e2d1445e84d8a3bc499d9ad83abbae98362245f892f59ca250a20d6fb36dbb8


## https://stackoverflow.com/questions/19335444/how-do-i-assign-a-port-mapping-to-an-existing-docker-container
# This is used for opening ports on a preexisting docker container. 

"PortBindings":{"110/tcp":[{"HostIp":"","HostPort":"110"}],"143/tcp":[{"HostIp":"","HostPort":"143"}],"22/tcp":[{"HostIp":"","HostPort":"10022"}],"25/tcp":[{"HostIp":"","HostPort":"25"}],"465/tcp":[{"HostIp":"","HostPort":"465"}],"587/tcp":[{"HostIp":"","HostPort":"587"}],"8080/tcp":[{"HostIp":"","HostPort":"80"}],"993/tcp":[{"HostIp":"","HostPort":"993"}],"995/tcp":[{"HostIp":"","HostPort":"995"}]}

"PortBindings":{"2379/tcp":[{"HostIp":"","HostPort":"2379"}],"2380/tcp":[{"HostIp":"","HostPort":"2380"}]}


etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380 --listen-peer-urls http://172.20.0.10:2380 --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:2379 --advertise-client-urls http://172.20.0.10:2379   --initial-cluster-token etcd-cluster-1 --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=http://172.20.0.12:2380 --initial-cluster-state new

docker run -d -h mail.example.org --name citadel --dns 8.8.8.8 -p 25:25 -p 110:110 -p 143:143 -p 465:465 -p 587:587 -p 993:993 -p 995:995 -p 80:8080 -p 10022:22 --env="ROOT_PASS=myrootpassword" --env="PASSWORD=mypassword" --env="DOMAIN=example.org" --env="ATOM_SUPPORT=true" million12/citadel

docker create -it --network pg_network --ip 172.20.0.10 -p 2379:2379 -p 2380:2380 -p 4001:4001 -p 5432:5432 -p 6432:6432 -h postgres1 --name postgres1 postgres15_ha_image

*** SPECIAL NOTE ***
# https://www.baeldung.com/ops/docker-compose-expose-vs-ports
# https://www.mend.io/free-developer-tools/blog/docker-expose-port/
# https://gist.github.com/ThinhPhan/9c57ef3d2717d499507aeb2bed8a65c4

-P option, or -p vs --expose

# First, let's look at the expose configuration. This property defines the ports that Docker Compose exposes from the container.
	These ports will be accessible by other services connected to the same network, but won't be published on the host machine.

# Now let's check the ports section. As with expose, this property defines the ports that we want to expose from the container. 
	But unlike with the expose configuration, these ports will be accessible internally and published on the host machine.

# Sources #
https://github.com/testdrivenio/django-on-docker
https://github.com/testdrivenio/fastapi-crud-async
https://ably.com/blog/no-we-dont-use-kubernetes



#
#
#### Sort this later ###
#
#




# Source: https://www.techsupportpk.com/2022/02/set-up-highly-available-postgresql-cluster-docker-ubuntu.html
# https://devopscube.com/setup-etcd-cluster-linux/
# https://github.com/etcd-io/etcd



sudo docker run -it --name postgres_release12 -e DEBIAN_FRONTEND=noninteractive ubuntu:20.04
sudo docker run -it --name postgres_release12
sudo docker commit postgres_release12 postgres15_ha_image
docker create -it --network pg_network --ip 172.20.0.12 -h postgres3 --name postgres3 postgres15_ha_image
sudo docker network create -d bridge --subnet=172.20.0.0/16 pg_network

192.168.240.3 docker_micro_1
192.168.240.6 docker_celery_1
192.168.240.5 docker_celery-beat_1
192.168.240.4 docker_web_1
192.168.240.2 docker_redis_1

172.20.0.10    postgres1
172.20.0.11    postgres2
172.20.0.12    postgres3


pg1: 10.80.80.195 and pg2: 10.80.80.196

etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380   --listen-peer-urls http://172.20.0.10:2380   --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:2379   --advertise-client-urls http://172.20.0.10:2379   --initial-cluster-token etcd-cluster-1   --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=172.20.0.12   --initial-cluster-state new
etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380 --listen-peer-urls http://172.20.0.10:2380 --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:2379 --advertise-client-urls http://172.20.0.10:2379 --initial-cluster-token etcd-cluster-1 --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=http://172.20.0.12:2380 --initial-cluster-state new

rm -rf /var/lib/etcd/* /etc/systemd/system/etcd*


postgres1 - 549530025adae0b18a0cd83c9eebd511e5df561b9d066d5aa9d51b19336aea3a
postgres2 - 35691a603696390ce48529924d7d2e3dea727225f8840a884b3576709bf37f27
postgres3 - ef07dcc9ac40e9681ba3fac0aabbe7fe1f6901b3c608f803bfceebe7eb6531c9

micro - 720544d735bad55679c17c0e9dcd0acb53eb0f0d141c9825eaeb2d002de6b40b
citadel - 4e2d1445e84d8a3bc499d9ad83abbae98362245f892f59ca250a20d6fb36dbb8


## https://stackoverflow.com/questions/19335444/how-do-i-assign-a-port-mapping-to-an-existing-docker-container
# This is used for opening ports on a preexisting docker container. 

"PortBindings":{"110/tcp":[{"HostIp":"","HostPort":"110"}],"143/tcp":[{"HostIp":"","HostPort":"143"}],"22/tcp":[{"HostIp":"","HostPort":"10022"}],"25/tcp":[{"HostIp":"","HostPort":"25"}],"465/tcp":[{"HostIp":"","HostPort":"465"}],"587/tcp":[{"HostIp":"","HostPort":"587"}],"8080/tcp":[{"HostIp":"","HostPort":"80"}],"993/tcp":[{"HostIp":"","HostPort":"993"}],"995/tcp":[{"HostIp":"","HostPort":"995"}]}

"PortBindings":{"2379/tcp":[{"HostIp":"","HostPort":"2379"}],"2380/tcp":[{"HostIp":"","HostPort":"2380"}]}


etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380 --listen-peer-urls http://172.20.0.10:2380 --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:2379 --advertise-client-urls http://172.20.0.10:2379   --initial-cluster-token etcd-cluster-1 --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=http://172.20.0.12:2380 --initial-cluster-state new

docker run -d -h mail.example.org --name citadel --dns 8.8.8.8 -p 25:25 -p 110:110 -p 143:143 -p 465:465 -p 587:587 -p 993:993 -p 995:995 -p 80:8080 -p 10022:22 --env="ROOT_PASS=myrootpassword" --env="PASSWORD=mypassword" --env="DOMAIN=example.org" --env="ATOM_SUPPORT=true" million12/citadel

sudo docker create -it --network pg_network --ip 172.20.0.10 --expose 2379 --expose 2380 --expose 4001 --expose 5432 --expose 6432 -h postgres1 --name postgres1 postgres15_ha_image



iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A INPUT -p tcp --dport 2379 -j ACCEPT
iptables -A INPUT -p tcp --dport 2380 -j ACCEPT
iptables -A INPUT -p tcp --dport 4001 -j ACCEPT
iptables -A INPUT -p tcp --dport 5432 -j ACCEPT
iptables -A INPUT -p tcp --dport 6432 -j ACCEPT






*** SPECIAL NOTE ***
# https://www.baeldung.com/ops/docker-compose-expose-vs-ports
# https://www.mend.io/free-developer-tools/blog/docker-expose-port/
# https://gist.github.com/ThinhPhan/9c57ef3d2717d499507aeb2bed8a65c4

-P option, or -p vs --expose

# First, let's look at the expose configuration. This property defines the ports that Docker Compose exposes from the container.
	These ports will be accessible by other services connected to the same network, but won't be published on the host machine.

# Now let's check the ports section. As with expose, this property defines the ports that we want to expose from the container. 
	But unlike with the expose configuration, these ports will be accessible internally and published on the host machine.
	


docker create -it --network pg_network --ip 172.20.0.10 --expose 6432 --expose 5432 --expose 4001 --expose 2380 --expose 2379 -h postgres1 --name postgres1 postgres15_ha_image 

docker create -it --network pg_network --ip 172.20.0.11 --expose 6432 --expose 5432 --expose 4001 --expose 2380 --expose 2379 -h postgres2 --name postgres2 postgres15_ha_image 

docker create -it --network pg_network --ip 172.20.0.12 --expose 6432 --expose 5432 --expose 4001 --expose 2380 --expose 2379 -h postgres3 --name postgres3 postgres15_ha_image 



-advertise-client-urls http://172.20.0.10:2379,http://172.20.0.10:4001 -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 -initial-advertise-peer-urls http://172.20.0.10:2380 -listen-peer-urls http://0.0.0.0:2380 -initial-cluster-token etcd-cluster-1 -initial-cluster etcd0=http://172.20.0.10:2380,etcd1=http://172.20.0.11:2380,etcd2=http://172.20.0.12:2380 -initial-cluster-state new



etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380 --listen-peer-urls http://172.20.0.10:2380 --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:2379 --advertise-client-urls http://172.20.0.10:2379 --initial-cluster-token etcd-cluster-1 --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=http://172.20.0.12:2380 --initial-cluster-state new
etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380 --listen-peer-urls http://172.20.0.10:2380 --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:2379 --advertise-client-urls http://172.20.0.10:2379 --initial-cluster-token etcd-cluster-1 --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=http://172.20.0.12:2380 --initial-cluster-state new
etcd --name postgres1 --initial-advertise-peer-urls http://172.20.0.10:2380 --listen-peer-urls http://172.20.0.10:2380 --listen-client-urls http://172.20.0.10:2379,http://127.0.0.1:4001 --advertise-client-urls http://172.20.0.10:2379 --initial-cluster-token etcd-cluster-1 --initial-cluster postgres1=http://172.20.0.10:2380,postgres2=http://172.20.0.11:2380,postgres3=http://172.20.0.12:2380 --initial-cluster-state new














	
	###
	
# https://etcd.io/docs/v2.3/docker_guide/#etcd0
# etcd0
	
docker run -d --expose 4001 --expose 2380 --expose 2379 \
 --name postgres1 quay.io/coreos/etcd:v2.3.8 \
 --name postgres1 \
 -advertise-client-urls http://172.20.0.10:2379,http://172.20.0.10:4001 \
 -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
 -initial-advertise-peer-urls http://172.20.0.10:2380 \
 -listen-peer-urls http://0.0.0.0:2380 \
 -initial-cluster-token etcd-cluster-1 \
 -initial-cluster etcd0=http://172.20.0.10:2380,etcd1=http://172.20.0.11:2380,etcd2=http://172.20.0.12:2380 \
 -initial-cluster-state new
 
# etcd1

docker run -d --expose 4001 --expose 2380 --expose 2379 \
 --name postgres2 quay.io/coreos/etcd:v2.3.8 \
 --name postgres2 \
 -advertise-client-urls http://172.20.0.11:2379,http://172.20.0.11:4001 \
 -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
 -initial-advertise-peer-urls http://172.20.0.11:2380 \
 -listen-peer-urls http://0.0.0.0:2380 \
 -initial-cluster-token etcd-cluster-1 \
 -initial-cluster etcd0=http://172.20.0.10:2380,etcd1=http://172.20.0.11:2380,etcd2=http://172.20.0.12:2380 \
 -initial-cluster-state new
 
 # etcd2
 
 docker run -d --expose 4001 --expose 2380 --expose 2379 \
 --name postgres3 quay.io/coreos/etcd:v2.3.8 \
 --name postgres3 \
 -advertise-client-urls http://172.20.0.12:2379,http://172.20.0.12:4001 \
 -listen-client-urls http://0.0.0.0:2379,http://0.0.0.0:4001 \
 -initial-advertise-peer-urls http://172.20.0.12:2380 \
 -listen-peer-urls http://0.0.0.0:2380 \
 -initial-cluster-token etcd-cluster-1 \
 -initial-cluster etcd0=http://172.20.0.10:2380,etcd1=http://172.20.0.11:2380,etcd2=http://172.20.0.12:2380 \
 -initial-cluster-state new