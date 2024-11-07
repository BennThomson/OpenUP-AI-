from django.urls import path
from .views import MainPage, contact_page

urlpatterns = [
    path('', MainPage, name='mainPage'),
    path('contact/', contact_page, name='contactPage'),
]