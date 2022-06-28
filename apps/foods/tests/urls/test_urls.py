from django.test import TestCase
from django.urls import reverse, resolve

from apps.foods.views import (
    FoodDetailView,
    FoodUpdateView,
    FoodListView,
    FoodCreateView,
    FoodDeleteView,
    RegistereFoodListView, 
    RegisteredFoodDeleteView, 
    FoodConsumedListView, 
    FoodConsumedRegisteredListView, 
    FoodConsumedDetailView, 
    FoodConsumedDeleteView, 
    DailyUserFoodStatsView, 
)


class TestUrls(TestCase):
    
    def test_list_foods_account_url_resolves(self):
        url = reverse("foods:list_foods")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodListView)

    def test_food_details_url_resolves(self):
        url = reverse("foods:food_details", kwargs={"slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodDetailView)

    def test_food_update_url_resolves(self):
        url = reverse("foods:food_update", kwargs={"slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodUpdateView)

    def test_food_create_url_resolves(self):
        url = reverse("foods:food_create")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodCreateView)
    
    def test_food_delete_url_resolves(self):
        url = reverse("foods:food_delete", kwargs={"slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodDeleteView)

    def test_list_registered_food_url_resolves(self):
        url = reverse("foods:registered_foods")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, RegistereFoodListView)
    
    def test_delete_registered_food_url_resolves(self):
        url = reverse("foods:register_food_delete", kwargs={"slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, RegisteredFoodDeleteView)

    def test_list_food_consumed_registered_url_resolves(self):
        url = reverse("foods:registered_food_consumed_list", kwargs={"food_registered_slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodConsumedRegisteredListView)

    def test_food_consumed_detail_url_resolves(self):
        url = reverse("foods:food_consumed_detail", kwargs={"pk": 1})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodConsumedDetailView)

    def test_delete_food_consumed_url_resolves(self):
        url = reverse("foods:delete_food_consumed", kwargs={"pk": 1})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodConsumedDeleteView)
    
    def test_list_daily_user_food_status_url_resolves(self):
        url = reverse("foods:food_consumed_daily_list")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, DailyUserFoodStatsView)
