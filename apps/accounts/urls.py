from re import template
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView

from .views import (
    RegisterView,
    CustomLoginView,
    ActivateAccountView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    ProfileDetailView,
)

app_name = "accounts"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        include(
            [
                path("", CustomLoginView.as_view(), name="login"),
                path(
                    "activate_account/<str:uidb64>/<str:token>",
                    ActivateAccountView.as_view(),
                    name="activate_account",
                ),
            ]
        ),
    ),
    path(
        "forgot_password/",
        CustomPasswordResetView.as_view(),
        name="reset_password_custom",
    ),
    path(
        "reset/<uidb64>/<token>",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("profile/<uuid:uuid>/", ProfileDetailView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", RedirectView.as_view(url="login")),
]
