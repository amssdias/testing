import copy

from django.test import TestCase
from django.urls import reverse
from django.core import mail

from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User


class RegistrateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="password123"
        )
        cls.register_url = reverse("accounts:register")
        cls.payload = {
            "email": "testing@gmail.com",
            "password1": "randompassword.1234",
            "password2": "randompassword.1234",
        }
        return super().setUpTestData()

    def test_GET_register_view_status_code(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_register_view_template_used(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, "accounts/pages/register.html")

    def test_GET_register_view_redirect_logged_user(self):
        self.client.login(username="test@testing.com", password="password123")
        response = self.client.get(self.register_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse("accounts:profile", kwargs={"uuid": self.user.profile.uuid}),
        )

    def test_GET_register_view_redirect_logged_user_template_used(self):
        self.client.login(username="test@testing.com", password="password123")
        response = self.client.get(self.register_url, follow=True)
        self.assertTemplateUsed(response, "accounts/pages/profile.html")

    def test_POST_register_view_status_code(self):
        response = self.client.post(
            self.register_url, self.payload, follow=True, secure=True
        )
        self.assertEqual(response.status_code, 200)

    def test_POST_register_view_redirect_code(self):
        response = self.client.post(
            self.register_url, self.payload, follow=True, secure=True
        )
        self.assertEqual(response.redirect_chain[0][1], 302)

    def test_POST_register_view_email_sent(self):
        self.client.post(self.register_url, self.payload, secure=True)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Activate your account")

    def test_POST_register_view_user_created(self):
        self.client.post(self.register_url, self.payload, secure=True)
        user = User.objects.get(email=self.payload["email"])
        self.assertTrue(user)

    def test_POST_register_view_profile_created(self):
        self.client.post(self.register_url, self.payload, secure=True)
        user_profile = Profile.objects.filter(user__email=self.payload["email"]).all()
        self.assertTrue(user_profile)
        self.assertEqual(user_profile.count(), 1)

    def test_POST_register_view_unmatching_password(self):
        wrong_password_payload = copy.deepcopy(self.payload)
        wrong_password_payload.update({"password2": "Testing456"})
        response = self.client.post(
            self.register_url, wrong_password_payload, secure=True
        )
        self.assertEqual(response.status_code, 400)
