from django.contrib import admin

from apps.foods.models import FoodConsumed
from apps.foods.models.food_consumed import (
    BreakfastConsumed,
    LunchConsumed,
    DinnerConsumed,
    DessertConsumed,
    SnacksConsumed,
)


@admin.register(FoodConsumed)
class FoodConsumedAdmin(admin.ModelAdmin):
    list_display = ("id", "registered_food", "meal", "grams", "created")


admin.site.register(BreakfastConsumed, FoodConsumedAdmin)
admin.site.register(LunchConsumed, FoodConsumedAdmin)
admin.site.register(DinnerConsumed, FoodConsumedAdmin)
admin.site.register(DessertConsumed, FoodConsumedAdmin)
admin.site.register(SnacksConsumed, FoodConsumedAdmin)
