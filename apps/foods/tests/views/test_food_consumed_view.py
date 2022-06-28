from django.test import TestCase
from django.urls import reverse

from apps.accounts.models.user import User
from apps.foods.models import Food, RegisteredFood, FoodConsumed


class TestFoodConsumedViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing123"
        )
        cls.food = Food.objects.create(name="Rice", brand="Bazmati", calories=350)
        cls.registered_food = RegisteredFood.objects.create(
            user_profile=cls.user.profile, food=cls.food
        )
        cls.food_consumed = FoodConsumed.objects.create(
            registered_food=cls.registered_food,
            grams=125,
            meal=FoodConsumed.DINNER,
        )
        cls.list_food_consumed_registered_url = reverse(
            "foods:registered_food_consumed_list",
            kwargs={"food_registered_slug": cls.registered_food.slug},
        )
        cls.detail_food_consumed = reverse(
            "foods:food_consumed_detail", kwargs={"pk": cls.food_consumed.id}
        )
        cls.delete_food_consumed = reverse(
            "foods:delete_food_consumed", kwargs={"pk": cls.food_consumed.id}
        )
        return super().setUpTestData()

    def test_GET_food_consumed_registered_list_view_status_code(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_food_consumed_registered_url)
        self.assertEqual(response.status_code, 200)

    def test_GET_food_consumed_registered_list_view_template_used(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.list_food_consumed_registered_url)
        self.assertTemplateUsed(response, "foods/foodconsumed_list.html")

    def test_GET_food_consumed_registered_list_view_not_authenticated(self):
        response = self.client.get(self.list_food_consumed_registered_url, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)

    def test_GET_food_consumed_detail_view_status_code(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.detail_food_consumed)
        self.assertEqual(response.status_code, 200)

    def test_GET_food_consumed_detail_view_template_used(self):
        self.client.login(username="test@testing.com", password="testing123")
        response = self.client.get(self.detail_food_consumed)
        self.assertTemplateUsed(response, "foods/foodconsumed_detail.html")

    def test_GET_food_consumed_detail_view_not_authenticated(self):
        response = self.client.get(self.detail_food_consumed, follow=True)
        self.assertEqual(response.redirect_chain[0][1], 302)
