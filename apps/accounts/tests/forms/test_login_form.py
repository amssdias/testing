from django.test import TestCase, RequestFactory
from django.urls import reverse

from apps.accounts.forms import LoginForm
from apps.accounts.models.user import User


class LoginFormTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testing", email="test@testing.com", password="1234Testing"
        )
        cls.data = {
            "username": "testing@gmail.com",
            "password": "1234Testing",
        }
        cls.form = LoginForm

    def setUp(self):
        self.form_data = {
            "username": "test@testing.com",
            "password": "1234Testing"
        }

    def test_login_form_email_label(self):
        self.assertEqual(self.form().fields["username"].label, "Email")

    def test_form_valid(self):
        login_form = self.form(data=self.form_data)
        self.assertTrue(login_form.is_valid())

    def test_form_no_data(self):
        login_form = self.form(data={})
        self.assertFalse(login_form.is_valid())

    def test_form_invalid_password(self):
        self.form_data["password"] = "wrong_password"
        login_form = self.form(data=self.form_data)
        self.assertFalse(login_form.is_valid())

    def test_form_invalid_email(self):
        self.form_data["username"] = "no_email@testing.com"
        login_form = self.form(data=self.form_data)
        self.assertFalse(login_form.is_valid())

    def test_form_invalid_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        factory = RequestFactory()
        request = factory.post(reverse("accounts:login"), data=self.form_data)
        login_form = self.form(data=self.form_data)
        login_form.request = request
        self.assertFalse(login_form.is_valid())
