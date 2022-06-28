from django.contrib import admin

from apps.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user_email", "weight", "uuid")
    readonly_fields = ("uuid",)
    fields = ()

    def user_email(self, profile):
        if profile.user:
            return profile.user.email
