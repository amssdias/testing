from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.accounts.models.profile import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = "accounts/pages/profile.html"
    model = Profile

    def get_object(self, queryset=None):
        return Profile.objects.select_related("user").get(uuid=self.kwargs.get("uuid"))

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        return context
