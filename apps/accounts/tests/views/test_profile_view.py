from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User


class TestProfileDetailView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing123"
        )
        cls.register_url = reverse(
            "accounts:profile", kwargs={"uuid": cls.user.profile.uuid}
        )
        return super().setUpTestData()

    def test_GET_profile_view_status_code(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_profile_view_template_used(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, "accounts/pages/profile.html")

    def test_GET_profile_view_not_authenticated(self):
        response = self.client.get(self.register_url, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
