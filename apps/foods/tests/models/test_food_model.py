from django.test import TestCase
from django.urls import reverse

from apps.foods.models import Food


class TestFoodModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.coca_cola = Food.objects.create(
            name="Coca Cola", brand="Coca-Cola", calories=100
        )

    def test_food_str(self):
        self.assertEqual(
            str(self.coca_cola), f"{self.coca_cola.name} - {self.coca_cola.brand}"
        )

    def test_food_absolute_url(self):
        url = reverse("foods:food_details", kwargs={"slug": self.coca_cola.slug})
        self.assertEqual(self.coca_cola.get_absolute_url(), url)
