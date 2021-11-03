from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save #signals are helpfull to create and save user
from django.dispatch import receiver # this is the trigger to create or save a new user
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User) # means "when there is any registration to the user"
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

    instance.profile.save()