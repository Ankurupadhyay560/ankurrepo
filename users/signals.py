from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import profile
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def profile_create(sender,instance,created,**kwargs):
    if(created):
        profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def profile_save(sender,instance,**kwargs):
    instance.profile.save()