from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

from apps.foods.models import RegisteredFood


class RegistereFoodListView(LoginRequiredMixin, ListView):
    model = RegisteredFood
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_profile=self.request.user.profile).select_related(
            "food"
        )


class RegisteredFoodDeleteView(LoginRequiredMixin, DeleteView):
    model = RegisteredFood
    success_url = reverse_lazy("foods:registered_foods")
