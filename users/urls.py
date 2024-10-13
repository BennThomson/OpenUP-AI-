from django.urls import path
from .views import user_login_view, user_register_view

urlpatterns = [
    path('login/', user_login_view, name='login'),
    path('register/', user_register_view, name='register'),
]

