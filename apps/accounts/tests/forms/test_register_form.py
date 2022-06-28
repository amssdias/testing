from django.core.exceptions import ValidationError
from django.test import TestCase, RequestFactory
from django.urls import reverse

from apps.accounts.forms import RegisterForm
from apps.accounts.models.profile import Profile
from apps.accounts.models.user import User


class RegistrationFormTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "email": "test@testing.com",
            "password1": "randompassword.1234",
            "password2": "randompassword.1234",
        }
        cls.register_form = RegisterForm(data=cls.data)

        cls.factory = RequestFactory()
        cls.request = cls.factory.post(reverse("accounts:register"), cls.data)
        cls.register_form.request = cls.request

        return super().setUpTestData()

    def test_form_valid(self):
        self.assertTrue(self.register_form.is_valid())

    def test_form_invalid_password(self):
        wrong_data = {
            "email": "testing@gmail.com",
            "password1": "5678Testing",
            "password2": "1234Testing",
        }
        register_form_invalid = RegisterForm(data=wrong_data)
        self.assertFalse(register_form_invalid.is_valid())
        self.assertTrue(register_form_invalid.has_error("password2"))
        self.assertEqual(len(register_form_invalid.errors), 1)

    def test_form_no_data(self):
        register_form_empty = RegisterForm(data={})
        self.assertFalse(register_form_empty.is_valid())

    def test_user_profile_created(self):
        self.register_form.is_valid()
        user = self.register_form.save()
        user_profile = Profile.objects.filter(user=user).exists()
        self.assertTrue(user_profile)

    def test_form_user_inactive(self):
        self.register_form.is_valid()
        user = self.register_form.save()
        self.assertFalse(user.is_active)

    def test_form_user_already_exists(self):
        User.objects.create_user(
            username="Test", email="test@testing.com", password="Testing123"
        )
        self.assertFalse(self.register_form.is_valid())
