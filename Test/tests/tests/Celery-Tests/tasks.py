from celery import Celery

app = Celery('tasks', backend='redis', broker='redis://')

@app.task
def print_hello():
    print('hello there')