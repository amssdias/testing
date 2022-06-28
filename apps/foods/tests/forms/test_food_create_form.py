from django.test import TestCase

from apps.foods.forms import FoodCreateForm
from apps.foods.models import Food


class TestRegistrationForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "name": "Rice",
            "brand": "Bazmati",
            "weight": 100,
            "calories": 100,
            "total_fat": 100,
            "carbs": 100,
            "fiber": 20,
            "protein": 15,
            "salt": 2,
        }
        return super().setUpTestData()

    def test_form_valid(self):
        food_create_form = FoodCreateForm(data=self.data)
        self.assertTrue(food_create_form.is_valid())

    def test_form_invalid_calories(self):
        wrong_data = self.data.copy()
        wrong_data["calories"] = 4321434.42
        food_create_form = FoodCreateForm(data=wrong_data)
        self.assertFalse(food_create_form.is_valid())
        self.assertTrue(food_create_form.has_error("calories"))
        self.assertEqual(len(food_create_form.errors), 1)

    def test_form_no_data(self):
        food_create_form = FoodCreateForm(data={})
        self.assertFalse(food_create_form.is_valid())

    def test_food_created(self):
        food_create_form = FoodCreateForm(data=self.data)
        food_create_form.save()
        food = Food.objects.filter(brand="Bazmati").exists()
        self.assertTrue(food)
