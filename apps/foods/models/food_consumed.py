from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.foods.models import RegisteredFood
from apps.foods.models.managers import FoodConsumedManager
from calorie_counter.models.abstracts import TimeStampable


class FoodConsumed(TimeStampable):
    BREAKFAST = "BKFT"
    LUNCH = "LNCH"
    DINNER = "DNNR"
    DESSERT = "DSST"
    SNACK = "SNCK"

    MEALS = (
        (BREAKFAST, _("Breakfast")),
        (LUNCH, _("Lunch")),
        (DINNER, _("Dinner")),
        (DESSERT, _("Dessert")),
        (SNACK, _("Snack")),
    )

    registered_food = models.ForeignKey(RegisteredFood, on_delete=models.CASCADE, related_name="consumed")
    grams = models.IntegerField()
    meal = models.CharField(max_length=4, choices=MEALS)

    class Meta:
        verbose_name = _("Food Consumed")
        verbose_name_plural = _("Foods Consumed")
        ordering = ["-created"]

    def __str__(self):
        return f"{self.registered_food.user_profile} - {self.registered_food.food} ({self.grams} Kg/Ml)"


class BreakfastConsumed(FoodConsumed):
    objects = FoodConsumedManager(FoodConsumed.BREAKFAST)

    class Meta:
        proxy = True
        verbose_name = _("Breakfast")
        verbose_name_plural = _("Breakfasts")


class LunchConsumed(FoodConsumed):
    objects = FoodConsumedManager(FoodConsumed.LUNCH)

    class Meta:
        proxy = True
        verbose_name = _("Lunch")
        verbose_name_plural = _("Lunches")


class DinnerConsumed(FoodConsumed):
    objects = FoodConsumedManager(FoodConsumed.DINNER)

    class Meta:
        proxy = True
        verbose_name = _("Dinner")
        verbose_name_plural = _("Dinners")


class DessertConsumed(FoodConsumed):
    objects = FoodConsumedManager(FoodConsumed.DESSERT)

    class Meta:
        proxy = True
        verbose_name = _("Dessert")
        verbose_name_plural = _("Desserts")


class SnacksConsumed(FoodConsumed):
    objects = FoodConsumedManager(FoodConsumed.SNACK)

    class Meta:
        proxy = True
        verbose_name = _("Snack registered")
        verbose_name_plural = _("Snacks registered")
