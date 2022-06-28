from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView

from apps.accounts.views import (
    RegisterView,
    CustomLoginView,
    ActivateAccountView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    ProfileDetailView,
)


class UrlsTestCase(SimpleTestCase):
    def test_register_url_resolves(self):
        url = reverse("accounts:register")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, RegisterView)

    def test_activate_account_url_resolves(self):
        url = reverse(
            "accounts:activate_account", kwargs={"uidb64": "MTE", "token": "abcde123"}
        )
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, ActivateAccountView)

    def test_login_url_resolves(self):
        url = reverse("accounts:login")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, CustomLoginView)

    def test_logout_url_resolves(self):
        url = reverse("accounts:logout")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, LogoutView)

    def test_password_reset_url_resolves(self):
        url = reverse("accounts:reset_password_custom")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, CustomPasswordResetView)

    def test_password_reset_confirm_url_resolves(self):
        url = reverse(
            "accounts:password_reset_confirm",
            kwargs={"uidb64": "MTE", "token": "abcde123"},
        )
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, CustomPasswordResetConfirmView)

    def test_profile_url_resolves(self):
        url = reverse(
            "accounts:profile", kwargs={"uuid": "9e6b25b3-7d6d-46c9-bf1c-e29279ff326d"}
        )
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, ProfileDetailView)
