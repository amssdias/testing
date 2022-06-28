from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import User


class UserAdminCustom(UserAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("id",)


admin.site.register(User, UserAdminCustom)
