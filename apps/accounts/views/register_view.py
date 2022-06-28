from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic.edit import CreateView

from apps.accounts.forms.register_form import RegisterForm


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "accounts/pages/register.html"
    success_url = reverse_lazy("accounts:login")
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            return redirect(
                "accounts:profile", uuid=self.request.user.profile.uuid, permanent=True
            )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.request = self.request
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def get_success_message(self, cleaned_data):
        return gettext("User created, check your email to activate your account.")
