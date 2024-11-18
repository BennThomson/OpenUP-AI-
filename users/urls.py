from django.urls import path
from .views import (
    user_login_view,
    user_register_view,
    user_logout_view,
    user_edit_view,
    CustomPasswordResetView,
)
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("login/", user_login_view, name="login"),
    path("register/", user_register_view, name="register"),
    path("logout/", user_logout_view, name="logout"),
    path("edit/<int:id>/", user_edit_view, name="edit"),
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
