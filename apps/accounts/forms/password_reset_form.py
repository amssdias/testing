from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext_lazy as _

from apps.accounts.models.user import User


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "login__form__input margin-bottom-small"})

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(_("Email is not registered. Register first."))
        else:
            return self.cleaned_data["email"]
