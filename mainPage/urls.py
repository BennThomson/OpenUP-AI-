from django.urls import path
from .views import MainPage, contact_page, text_checker, article_detail

urlpatterns = [
    path("", MainPage, name="mainPage"),
    path("contact/", contact_page, name="contactPage"),
    path("text_checker/", text_checker, name="text_checker"),
    path("article/<int:pk>/", article_detail, name="article_detail"),
]
