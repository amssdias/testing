from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.accounts.models.profile import Profile
from apps.foods.models.abstracts.food_nutrition import FoodNutrition


class Food(FoodNutrition):
    name = models.CharField(max_length=70)
    brand = models.CharField(max_length=70, null=True, blank=True)
    weight = models.IntegerField(default=100, help_text=_("g/ml"))
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    created_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="created_foods",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.brand}"

    def get_absolute_url(self):
        url = reverse("foods:food_details", kwargs={"slug": self.slug})
        return url
