from django.db import models


class FoodNutrition(models.Model):
    calories = models.DecimalField(max_digits=8, decimal_places=2)
    total_fat = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    carbs = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    fiber = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    protein = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    salt = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    class Meta:
        abstract = True
