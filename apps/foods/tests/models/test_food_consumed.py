from django.test import TestCase

from apps.accounts.models import User
from apps.foods.models import Food, RegisteredFood, FoodConsumed


class TestFoodModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing123"
        )
        cls.coca_cola = Food.objects.create(
            name="Coca Cola", brand="Coca-Cola", calories=100
        )
        cls.food_registered = RegisteredFood.objects.create(
            user_profile=cls.user.profile,
            food=cls.coca_cola,
        )
        cls.food_consumed = FoodConsumed.objects.create(
            registered_food=cls.food_registered, grams=25, meal=FoodConsumed.DINNER
        )

    def test_food_consumed_str(self):
        self.assertEqual(
            str(self.food_consumed),
            f"{self.food_consumed.registered_food.user_profile} - {self.food_consumed.registered_food.food} ({self.food_consumed.grams} Kg/Ml)",
        )
