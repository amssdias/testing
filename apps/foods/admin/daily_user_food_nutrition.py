from django.contrib import admin

from apps.foods.models import DailyUserFoodStatus


@admin.register(DailyUserFoodStatus)
class DailyUserFoodStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "date")
