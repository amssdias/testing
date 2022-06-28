from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.foods.models import Food


class TestRegisteredFoodViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing123"
        )
        cls.food = Food.objects.create(name="Rice", brand="Bazmati", calories=350)
        cls.list_registeredfood_url = reverse("foods:registered_foods")
        return super().setUpTestData()

    def test_GET_registered_foods_list_view_status_code(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_registeredfood_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_registered_foods_list_view_template_used(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_registeredfood_url)
        self.assertTemplateUsed(response, "foods/registeredfood_list.html")

    def test_GET_registered_foods_list_view_not_authenticated(self):
        response = self.client.get(self.list_registeredfood_url, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
