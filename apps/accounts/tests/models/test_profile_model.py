from django.test import TestCase

from apps.accounts.models.user import User


class ProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing1234"
        )
        cls.profile = cls.user.profile

    def test_user_label(self):
        field_label = self.profile._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_user_null(self):
        field_null = self.profile._meta.get_field("user").null
        self.assertTrue(field_null)

    def test_user_blank(self):
        field_blank = self.profile._meta.get_field("user").blank
        self.assertTrue(field_blank)

    def test_weight_label(self):
        field_label = self.profile._meta.get_field("weight").verbose_name
        self.assertEqual(field_label, "weight")

    def test_weight_null(self):
        field_null = self.profile._meta.get_field("weight").null
        self.assertTrue(field_null)

    def test_weight_blank(self):
        field_blank = self.profile._meta.get_field("weight").blank
        self.assertTrue(field_blank)

    def test_weight_target_label(self):
        field_label = self.profile._meta.get_field("weight_target").verbose_name
        self.assertEqual(field_label, "weight target")

    def test_weight_target_null(self):
        field_null = self.profile._meta.get_field("weight_target").null
        self.assertTrue(field_null)

    def test_weight_target_blank(self):
        field_blank = self.profile._meta.get_field("weight_target").blank
        self.assertTrue(field_blank)

    def test_uuid_target_label(self):
        field_label = self.profile._meta.get_field("uuid").verbose_name
        self.assertEqual(field_label, "uuid")

    def test_profile_str(self):
        self.assertEqual(str(self.profile), f"Profile {self.user}")
