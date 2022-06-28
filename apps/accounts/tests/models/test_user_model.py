from django.test import TestCase

from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing1234"
        )

    def test_signal_profile_was_created(self):
        self.assertTrue(Profile.objects.get(user=self.user))

    def test_user_str(self):
        self.assertEqual(str(self.user), "test@testing.com")
