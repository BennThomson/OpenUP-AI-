from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _


class humanized_texts_model(models.Model):
    original_text = models.TextField(_("original text"))
    humanized_text = models.TextField(_("humanized text"))

    def __str__(self):
        return f"{self.original_text[:20]}..."

    class Meta:
        verbose_name = _("text")
        verbose_name_plural = _("texts")
        db_table = "texts"


class saved_documents(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_("user")
    )
    text = models.ForeignKey(
        humanized_texts_model, on_delete=models.CASCADE, verbose_name=_("text")
    )
    number_of_words = models.PositiveBigIntegerField(_("number of words"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    purpose = models.CharField(_("purpose"), max_length=500)

    def __str__(self):
        return _("%(first_name)s Document") % {"first_name": self.user.first_name}

    class Meta:
        verbose_name = _("document")
        verbose_name_plural = _("documents")
        db_table = "documents"


class content_artices_model(models.Model):
    class TextChoices(models.TextChoices):
        BLOG_CONTENT = "Blog content", _("Blog content")
        CONTENT_WRITE = "Content write", _("Content write")
        NEWS_CONTENT = "News content", _("News content")
        SCIENTIFIC_CONTENT = "Scientific content", _("Scientific content")
        EDUCATIONAL_CONTENT = "Educational content", _("Educational content")
        OTHER = "Other", _("Other")

    type = models.CharField(_("type"), max_length=50, choices=TextChoices.choices)
    title = models.CharField(_("title"), max_length=500)
    content = models.TextField(_("content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))
    image = models.ImageField(
        _("image"), upload_to="articles/images", blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        db_table = "articles"


class Billing_model(models.Model):
    class TypeChoices(models.TextChoices):
        Monthly = "Monthly", _("Monthly")
        Yearly = "Yearly", _("Yearly")

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_("user")
    )
    paid_date = models.DateField(_("paid date"), auto_now_add=True)
    expire_date = models.DateField(_("expire date"), blank=True, null=True)
    type = models.CharField(_("type"), max_length=20, choices=TypeChoices.choices)
    how_much = models.PositiveSmallIntegerField(
        _("how much"), validators=[MinValueValidator(1), MaxValueValidator(500)]
    )

    def __str__(self):
        return f"{self.user}'s Billing'"

    class Meta:
        verbose_name = _("billing")
        verbose_name_plural = _("billings")
        db_table = "billings"
