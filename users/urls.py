from django.urls import path
from .views import user_login_view, user_register_view, reset_password_view, user_logout_view, user_edit_view

urlpatterns = [
    path('login/', user_login_view, name='login'),
    path('register/', user_register_view, name='register'),
    path('logout/', user_logout_view, name='logout'),
    path('edit/<int:id>/', user_edit_view, name='edit'),
    path('reset_password/', reset_password_view, name='reset-password'),
]

