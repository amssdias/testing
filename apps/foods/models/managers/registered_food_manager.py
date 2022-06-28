from django.db import models


class FoodConsumedManager(models.Manager):
    def __init__(self, meal: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meal = meal

    def get_queryset(self):
        return super().get_queryset().filter(meal=self.meal)
