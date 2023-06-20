from django.db.models.signals import pre_delete, post_delete
from .models import Event
from django.dispatch import receiver


@receiver(pre_delete, sender=Event)
def pre_delete_event(sender, **kwargs):
    print("You are about to delete something!")

@receiver(post_delete, sender=Event)
def delete_event(sender, **kwargs):
    print("You are about to delete something!")


# Notes
# REmember to import this into the apps.py file, see UI/apps.py
# that setting is as follows:
#    def ready(self):
#        from . import signals