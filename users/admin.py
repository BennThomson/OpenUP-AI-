from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation.trans_real import activate

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, ProfileModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "type_of_plan", "active"]
    list_filter = ["type_of_plan", "active", "id"]
    search_fields = ["id", "user__first_name"]
    readonly_fields = ["type_of_plan", "active"]
