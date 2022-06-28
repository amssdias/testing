from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import Profile 
from apps.foods.models.abstracts import FoodNutrition


class DailyUserFoodStatus(FoodNutrition):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="daily_status")
    date = models.DateField()

    class Meta:
        verbose_name = _("Daily User Food Status")
        verbose_name_plural = _("Daily User Food Status")
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(fields=["user_profile", "date"], name="unique_daily_user_stats")
        ]

    def __str__(self):
        return f"{self.user_profile.user.email} - {self.date}"
