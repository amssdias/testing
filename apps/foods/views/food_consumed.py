from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.list import ListView

from apps.foods.forms import FoodConsumedCreateForm
from apps.foods.models import FoodConsumed
from calorie_counter.utils import rule_of_three


class FoodConsumedListView(LoginRequiredMixin, ListView):
    """
    Probably delete this View
    """
    model = FoodConsumed
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(registered_food__user_profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FoodConsumedRegisteredListView(LoginRequiredMixin, ListView):
    model = FoodConsumed
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        registered_food_slug = self.kwargs.get("food_registered_slug", "")
        return queryset.filter(
            registered_food__user_profile__user=self.request.user,
            registered_food__slug=registered_food_slug,
        )


class FoodConsumedDetailView(LoginRequiredMixin, DetailView):
    model = FoodConsumed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food_consumed_values"] = self.get_food_consumed_values(
            context["object"]
        )
        return context

    def get_food_consumed_values(self, food_consumed: FoodConsumed):
        food_grams = food_consumed.grams
        food = food_consumed.registered_food.food
        food_weight = food.weight

        return {
            "calories": rule_of_three(food.calories, food_grams, food_weight),
            "total_fat": rule_of_three(food.total_fat, food_grams, food_weight),
            "carbs": rule_of_three(food.carbs, food_grams, food_weight),
            "fiber": rule_of_three(food.fiber, food_grams, food_weight),
            "protein": rule_of_three(food.protein, food_grams, food_weight),
            "salt": rule_of_three(food.salt, food_grams, food_weight),
        }


class FoodConsumedCreateView(LoginRequiredMixin, CreateView):
    model = FoodConsumed
    template_name_suffix = "_create"
    form_class = FoodConsumedCreateForm
    success_url = reverse_lazy("foods:food_consumed_list")

    def get_form_kwargs(self):
        """
        Send request to form.__init__ so we can show the form with filtered foods
        """
        kwargs = super(FoodConsumedCreateView, self).get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs

    def form_valid(self, form):
        form.request = self.request
        return super().form_valid(form)


class FoodConsumedDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = FoodConsumed
    success_url = reverse_lazy("foods:food_consumed_daily_list")
    success_message = _("Food was delete")

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url
