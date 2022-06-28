from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.shortcuts import render, redirect
from django.views import View

from apps.accounts.models.user import User
from apps.accounts.utils import generate_token


class ActivateAccountView(View):
    template_name = "accounts/email/activation_failed.html"
    token_generator = generate_token

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("accounts:login")

        return render(request, self.template_name, status=400)
