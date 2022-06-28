from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.accounts.views.password_reset_view import CustomPasswordResetView


class TestPasswordResetView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="1234test"
        )
        cls.reset_password_url = reverse("accounts:reset_password_custom")
        return super().setUpTestData()

    def test_GET_password_reset_view(self):
        response = self.client.get(self.reset_password_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "accounts/password-reset/password_reset_form.html"
        )

    def test_POST_password_reset_view_status_code(self):
        payload = {
            "email": "test@testing.com",
        }
        response = self.client.post(self.reset_password_url, payload, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_POST_password_reset_view_redirect(self):
        payload = {
            "email": "test@testing.com",
        }
        response = self.client.post(self.reset_password_url, payload, follow=True)
        self.assertEqual(response.redirect_chain[0][0], reverse("accounts:login"))

    def test_POST_password_reset_view_wrong_email(self):
        payload = {"email": "testing_wrong@gmail.com"}
        response = self.client.post(
            self.reset_password_url, payload, follow=True, secure=True
        )
        self.assertFalse(response.context_data["form"].is_valid())
        self.assertEqual(response.status_code, 400)
