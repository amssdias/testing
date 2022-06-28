from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User


class LoginViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="password123"
        )
        cls.login_url = reverse("accounts:login")
        return super().setUpTestData()

    def test_GET_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_login_view_template_used(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, "accounts/pages/login.html")

    def test_GET_login_view_logged_user(self):
        self.client.login(username="test@testing.com", password="password123")
        response = self.client.get(self.login_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse("accounts:profile", kwargs={"uuid": self.user.profile.uuid}),
        )

    def test_GET_login_view_logged_user_template_used(self):
        self.client.login(username="test@testing.com", password="password123")
        response = self.client.get(self.login_url, follow=True)
        self.assertTemplateUsed(response, "accounts/pages/profile.html")

    def test_POST_login_view_status_code(self):
        payload = {
            "email": self.user.email,
            "password": self.user.password,
        }
        response = self.client.post(self.login_url, payload, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_POST_login_view_inactive_user(self):
        self.user.is_active = False
        self.user.save()

        payload = {
            "email": "test_wrong@testing.com",
            "password": "password123",
        }
        response = self.client.post(self.login_url, payload, follow=True, secure=True)

        # By default django sends a status code of 200 for invalid credentials or some error to login
        # Therefore we can check for some errors
        self.assertFalse(self.user.is_active)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/login.html")
        self.assertTrue("invalid_login" in response.context_data["form"].error_messages)
        self.assertFalse(response.context_data["form"].is_valid())

    def test_POST_login_view_wrong_password(self):
        payload = {
            "email": "test@testing.com",
            "password": "wrong_password",
        }
        response = self.client.post(self.login_url, payload, follow=True)

        # By default django sends a status code of 200 for invalid credentials or some error to login
        # Therefore we can check for some errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/login.html")
        self.assertTrue("invalid_login" in response.context_data["form"].error_messages)
        self.assertFalse(response.context_data["form"].is_valid())

    def test_POST_login_view_wrong_email(self):
        payload = {
            "email": "wrong_test@testing.com",
            "password": "wrong_password",
        }
        response = self.client.post(self.login_url, payload, follow=True)

        # By default django sends a status code of 200 for invalid credentials or some error to login
        # Therefore we can check for some errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/pages/login.html")
        self.assertTrue("invalid_login" in response.context_data["form"].error_messages)
        self.assertFalse(response.context_data["form"].is_valid())
