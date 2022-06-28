from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from apps.foods.models.daily_user_food_status import DailyUserFoodStatus


class DailyUserFoodStatsView(LoginRequiredMixin, ListView):
    model = DailyUserFoodStatus
    template_name = "foods/daily_user_food_stats_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_profile=self.request.user.profile).order_by("-date")
