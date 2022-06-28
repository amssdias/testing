from django.db import models
from django.utils import timezone

class TimeStampable(models.Model):
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
