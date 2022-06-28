from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.accounts.models.user import User
from apps.accounts.utils import generate_token


class TestActivateAccountView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testing", email="testing@gmail.com", password="Testing123"
        )
        cls.user_1 = User.objects.create_user(
            username="testing1", email="testing1@gmail.com", password="Testing123"
        )
        return super().setUpTestData()

    def test_GET_activate_account_view(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = reverse(
            "accounts:activate_account",
            kwargs={
                "uidb64": uid,
                "token": generate_token.make_token(self.user),
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_GET_activate_account_view_wrong_token(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = reverse(
            "accounts:activate_account",
            kwargs={
                "uidb64": uid,
                "token": generate_token.make_token(self.user_1),
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, "accounts/email/activation_failed.html")

    def test_GET_activate_account_view_wrong_uid(self):
        uid = urlsafe_base64_encode(force_bytes(self.user_1.pk))
        url = reverse(
            "accounts:activate_account",
            kwargs={
                "uidb64": uid,
                "token": generate_token.make_token(self.user),
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, "accounts/email/activation_failed.html")

    def test_GET_activate_account_view_user_active(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        url = reverse(
            "accounts:activate_account",
            kwargs={
                "uidb64": uid,
                "token": generate_token.make_token(self.user),
            },
        )
        response = self.client.get(url)
        self.assertTrue(self.user.is_active)
        self.assertEqual(response.status_code, 302)

    def test_GET_activate_account_view_exception(self):
        uid = urlsafe_base64_encode(force_bytes(self.user_1.pk))
        url = reverse(
            "accounts:activate_account",
            kwargs={
                "uidb64": "786",
                "token": generate_token.make_token(self.user),
            },
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, "accounts/email/activation_failed.html")