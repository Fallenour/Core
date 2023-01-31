# project/tasks/sample_tasks.py

import time

from celery import shared_task


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

########################### Section #2 ######################################################

#from celery.decorators import task
#from celery.task.schedules import crontab
#from celery.decorators import periodic_task
#from celery.utils.log import get_task_logger

#from advpanel.emails import send_feedback_email

#logger = get_task_logger(__name__)

#@task(name="send_feedback_email_task")
#def send_feedback_email_task(email, message):
#    """sends an email when feedback form is filled successfully"""
#    logger.info("Sent feedback email")
#    return send_feedback_email(email, message)

#@periodic_task(
#    run_every=(crontab(minute='*/15')),
#    name="task_save_latest_flickr_image",
#    ignore_result=True
#)
#def task_save_latest_flickr_image():
#    """
#    Saves latest image from Flickr
#    """
#    save_latest_flickr_image()
#    logger.info("Saved image from Flickr")

####################### Section #3 ###############################################################

#from celery import Celery


#app = Celery('tasks', backend='redis', broker='redis://')


#@app.task
#def print_hello():
#    print('hello there')

###################################################################################################