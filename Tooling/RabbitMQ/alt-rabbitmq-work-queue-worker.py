#!/usr/bin/env python


# RabbitMQ Imports

import pika
import time
import subprocess
import os


# Django Imports

import django
from django.db import models


# Ground work for django, import django setup, configure connecting to Django ORM

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()



# Import Django Data Models once Django is Setup
from advpanel.models import System, Event


# Begin RabbitMQ Setup
## RabbitMQ Messaging
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
#    time.sleep(body.count(b'.'))
    # Split the message into components
    msplit = body.decode("utf-8")
#    print(msplit)
    msplit = body.split()
    print("Message Split : %r" % msplit)
    print("Item Isolated : %r" % msplit[1])
    Zone = msplit[1]
    decodedZone = Zone.decode("utf-8")
    print("Zone Isolated : %r" % decodedZone)
    zoneeventslist = Event.objects.get(zone=decodedZone)
#    zoneevents = decodedZone.event_set.all()
    print("Zone Events : %r" % zoneeventslist)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
#    return decodedZone
    zoneevents(decodedZone)


def zoneevents(decodedZone):
    zoneeventslist = Event.objects.get(zone=decodedZone)
    print("Zone Events inside Zone Events Function : %r" % zoneeventslist)
    zoneeventsdecoded = str(zoneeventslist)
    print("Zone Events inside Zone Events Function decoded : %r" % zoneeventsdecoded)
    zoneeventencoded = bytearray(zoneeventsdecoded, 'utf-8')
    zoneeventsdecoded = zoneeventencoded.decode("utf-8")
    msplit = zoneeventsdecoded.split()

    splitspace = msplit[1]
#    emptyspace = zoneeventsdecoded[0]
    payload =  msplit[1]
    function = msplit[10]
#    print("splitspace decoded Isolated : %r" % splitspace)
#    print("Emptyspace Encoded Item Isolated : %r" % zoneeventencoded)
#    print("Emptyspace Decoded Item Isolated : %r" % zoneeventsdecoded)
    print("Payload Item Isolated : %r" % payload)
    print(" Function Item Isolated : %r" % function)
    subprocesscalls(payload, function)


def subprocesscalls(payload, function):
    payload = payload
    function = function
    subprocess.call(["pwsh", "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/install-atomicredteam.ps1')", "Install-AtomicRedTeam"])
    subprocess.call(["pwsh", "-Command", function, payload])
    print(" [x] Done")


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()

### Notes on Rabbit ###
# https://riptutorial.com/python/example/11593/how-to-consume-messages-from-rabbitmq
# https://www.rabbitmq.com/tutorials/tutorial-two-python.html