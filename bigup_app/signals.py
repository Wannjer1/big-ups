from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# create_profile is the receiver function which is run every time a user is created.
# create_profile hecks if a user is created and then creates a profile to connect the two via the OneToOneField
# User is the sender which is responsible for making the notification


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# post_save is the signal that is sent at the end of the save method
# save_profile saves the User's Profile information whenever a user is saved
# after the User model's save() method has finished executing, it sends a signal(post_save) to the receiver function (create_profile) then this function will receive the signal to create and save a profile instance for that user.
