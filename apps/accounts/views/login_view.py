from django.contrib.auth.views import LoginView
from django.urls import reverse

from apps.accounts.forms.login_form import LoginForm


class CustomLoginView(LoginView):
    template_name = "accounts/pages/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        url = reverse(
            "accounts:profile", kwargs={"uuid": self.request.user.profile.uuid}
        )
        return url
