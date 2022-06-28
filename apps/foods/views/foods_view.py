from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

from apps.foods.forms import FoodCreateForm
from apps.foods.models.food import Food


class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name_suffix = "_list"
    ordering = "created_by"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            Q(created_by=self.request.user.profile) | Q(created_by__isnull=True)
        ).select_related("created_by__user")

    def get_ordering(self):
        ordering = self.request.GET.get("ordering", "created_by")
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food
    template_name_suffix = "_detail"

    def get_object(self, queryset=None):
        food = Food.objects.select_related("created_by__user").get(
            slug=self.kwargs.get("slug")
        )
        return food


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    form_class = FoodCreateForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return self.object.get_absolute_url()


class FoodCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Food
    form_class = FoodCreateForm
    success_url = reverse_lazy("foods:list_foods")
    success_message = _("Food was created successfully")

    def form_valid(self, form):
        food = form.save(commit=False)
        food.created_by = self.request.user.profile
        food.save()
        return super().form_valid(form)


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = reverse_lazy("foods:list_foods")
