from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy

from apps.accounts.forms.password_reset_form import CustomPasswordResetForm


class CustomPasswordResetView(PasswordResetView):
    """
    Ask the user for his email and send him an email with a link to reset his password
    """

    form_class = CustomPasswordResetForm
    email_template_name = "accounts/password-reset/password_reset_email.html"
    template_name = "accounts/password-reset/password_reset_form.html"
    success_url = reverse_lazy("accounts:login")

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Ask the user for the new password.
    """

    template_name = "accounts/password-reset/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:login")
