from django.contrib import admin

from apps.foods.models import RegisteredFood


class RegisteredFoodAdminCustom(admin.ModelAdmin):
    list_display = ("get_user", "food")
    readonly_fields = ("slug",)

    @admin.display(description="User")
    def get_user(self, obj):
        return obj.user_profile.user.username


admin.site.register(RegisteredFood, RegisteredFoodAdminCustom)
