from django.contrib import admin

from .models import ContactModel, FaqsModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_filter = ["name", "email"]


@admin.register(FaqsModel)
class FaqsModelAdmin(admin.ModelAdmin):
    search_field = ["question"]
    list_display = ["id", "question", "answer"]
