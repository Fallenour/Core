import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Settings.base")

app = Celery("Core", result_backend='django-db')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()