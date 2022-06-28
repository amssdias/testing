from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
