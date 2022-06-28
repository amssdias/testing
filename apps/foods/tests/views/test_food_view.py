from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.foods.models import Food


class TestProfileDetailView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing123"
        )
        cls.food = Food.objects.create(name="Rice", brand="Bazmati", calories=350)
        cls.list_foods_url = reverse("foods:list_foods")
        cls.detail_food_url = reverse("foods:food_details", kwargs={"slug": cls.food.slug})
        cls.update_food_url = reverse("foods:food_update", kwargs={"slug": cls.food.slug})
        return super().setUpTestData()

    def test_GET_foods_list_view_status_code(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_foods_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_foods_list_view_template_used(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_foods_url)
        self.assertTemplateUsed(response, "foods/food_list.html")

    def test_GET_foods_list_view_not_authenticated(self):
        response = self.client.get(self.list_foods_url, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)

    def test_GET_foods_details_view_status_code(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.detail_food_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_foods_details_view_template_used(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.detail_food_url)
        self.assertTemplateUsed(response, "foods/food_detail.html")

    def test_GET_foods_details_view_not_authenticated(self):
        response = self.client.get(self.detail_food_url, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
