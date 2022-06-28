from django.test import TestCase

from apps.accounts.forms import CustomPasswordResetForm
from apps.accounts.models.user import User


class CustomPasswordResetFormTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="Test", email="test@testing.com", password="Testing123"
        )

        cls.form = CustomPasswordResetForm
        cls.data = {"email": "test@testing.com"}
        return super().setUpTestData()

    def test_form_valid(self):
        custom_password_reset_form = self.form(data=self.data)
        self.assertTrue(custom_password_reset_form.is_valid())

    def test_form_invalid_no_data(self):
        custom_password_reset_form_no_data = self.form(data={})
        self.assertFalse(custom_password_reset_form_no_data.is_valid())

    def test_form_invalid_email(self):
        custom_password_reset_form_no_user = self.form(
            data={"email": "noemail@testing.com"}
        )
        self.assertFalse(custom_password_reset_form_no_user.is_valid())
