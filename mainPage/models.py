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

    def save(self, *args, **kwargs):
        if self.name == "benn":
            account_sid = "ACc006c1b0ddd4d4557f57d8b459333452"
            auth_token = "d77ea2b6a8e39f78f1f8fdca34f927b2"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"Message from {self.email}",
                from_="+14242275437",
                to="+998992190535",
            )
            print(message.sid, "*" * 30)
        return super().save(*args, **kwargs)


class FaqsModel(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return f"Question: {self.question}"

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        db_table = "faqs"
