from django.urls import path

from apps.foods.views import ( 
    FoodDetailView, 
    FoodListView, 
    FoodUpdateView, 
    FoodCreateView, 
    FoodDeleteView,
    RegistereFoodListView,
    RegisteredFoodDeleteView,
    FoodConsumedListView, 
    FoodConsumedRegisteredListView, 
    FoodConsumedDetailView, 
    FoodConsumedCreateView, 
    FoodConsumedDeleteView, 
    DailyUserFoodStatsView,
)


app_name = "foods"
urlpatterns = [
    path("all_foods/", FoodListView.as_view(), name="list_foods"),
    path("create_new_food/", FoodCreateView.as_view(), name="food_create"),
    path("detail/<slug:slug>", FoodDetailView.as_view(), name="food_details"),
    path("update/<slug:slug>", FoodUpdateView.as_view(), name="food_update"),
    path("delete/<slug:slug>", FoodDeleteView.as_view(), name="food_delete"),

    path("registered_foods/", RegistereFoodListView.as_view(), name="registered_foods"),
    path("delete_registered_food/<slug:slug>", RegisteredFoodDeleteView.as_view(), name="register_food_delete"),

    path("food_consumed_daily/", DailyUserFoodStatsView.as_view(), name="food_consumed_daily_list"), 
    # path("food_consumed/", FoodConsumedListView.as_view(), name="food_consumed_list"), 
    path("food_consumed/<slug:food_registered_slug>", FoodConsumedRegisteredListView.as_view(), name="registered_food_consumed_list"), 
    path("food_consumed/details/<int:pk>", FoodConsumedDetailView.as_view(), name="food_consumed_detail"), 
    path("food_consumed/create/", FoodConsumedCreateView.as_view(), name="food_consumed_create"), 
    path("food_consumed/delete/<int:pk>", FoodConsumedDeleteView.as_view(), name="delete_food_consumed"), 
]
