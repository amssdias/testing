from django.contrib import admin

from apps.foods.models import Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "get_user")
    readonly_fields = ("slug",)

    @admin.display(description="created by")
    def get_user(self, obj):
        return obj.created_by.user.email if obj.created_by else obj.created_by
