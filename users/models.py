from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    email_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ProfileModel(models.Model):
    class PlanChoices(models.TextChoices):
        FREE = "Free", _("Free")
        PREMIUM = "Premium", _("Premium")

    user = models.OneToOneField(
        "CustomUser", on_delete=models.CASCADE, verbose_name=_("user")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))
    type_of_plan = models.CharField(
        _("type of plan"),
        choices=PlanChoices.choices,
        max_length=10,
        default=PlanChoices.FREE,
    )
    available_words = models.PositiveIntegerField(_("available words"), default=5000)
    active = models.BooleanField(_("active"), default=True)

    def __str__(self):
        return _("%(first_name)s %(last_name)s Profile") % {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
        }

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        db_table = "profiles"
