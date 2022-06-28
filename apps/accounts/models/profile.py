import uuid
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="profile"
    )
    weight = models.FloatField(null=True, blank=True)
    weight_target = models.FloatField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"Profile {self.user}"
