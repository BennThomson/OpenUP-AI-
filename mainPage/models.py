from django.db import models
from twilio.rest import Client


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message by {self.email}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        db_table = "contacts"



class FaqsModel(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return f"Question: {self.question}"

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        db_table = "faqs"
