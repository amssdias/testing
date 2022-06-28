from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import Profile
from apps.foods.models.food import Food


class RegisteredFood(models.Model):
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="registered_foods"
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, null=True, related_name="registered_by_users"
    )
    slug = models.SlugField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("Registered Food")
        verbose_name_plural = _("Registered Foods")
        constraints = [
            models.UniqueConstraint(fields=["user_profile", "food"], name="unique_user_food")
        ]

    def __str__(self):
        return f"{self.food.name} - {self.food.brand}"
