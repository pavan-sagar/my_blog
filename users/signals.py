#Signals are used to trigger an action upon an event

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile 

#This watches for the post save signal that is raised while a new user registration is filled and submitted. The receiver decorator will create an instance of the Profile db.
@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#This will save the record in the Profile DB
@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()