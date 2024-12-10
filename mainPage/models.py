from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"))
    message = models.TextField(_("message"))

    def __str__(self):
        return _("Message by %(email)s") % {"email": self.email}

    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")
        db_table = "contacts"


class FaqsModel(models.Model):
    question = models.CharField(_("question"), max_length=100)
    answer = models.TextField(_("answer"))

    def __str__(self):
        return _("Question: %(question)s") % {"question": self.question}

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        db_table = "faqs"
