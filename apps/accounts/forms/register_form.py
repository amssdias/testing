from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext_lazy as _

from apps.accounts.models.user import User
from apps.accounts.tasks.send_email import send_email_async

from calorie_counter.utils.celery import task_celery


class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "login__form__input margin-bottom-xsmall"}))

    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "login__form__input margin-bottom-xsmall"})
        self.fields["password2"].widget.attrs.update({"class": "login__form__input margin-bottom-small"})

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("User with that email already exists."))
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.username = user.email
        if commit:
            user.save()

            current_site = get_current_site(self.request)
            task_celery(send_email_async, user_id=user.id, domain=current_site.domain)
        return user
