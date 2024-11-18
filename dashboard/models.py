from django.db import models
from users.models import CustomUser


class humanized_texts_model(models.Model):
    original_text = models.TextField()
    humanized_text = models.TextField()

    def __str__(self):
        return f"{self.original_text[20]}..."

    class Meta:
        verbose_name = "text"
        verbose_name_plural = "texts"
        db_table = "texts"


class saved_documents(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.ForeignKey(humanized_texts_model, on_delete=models.CASCADE)
    number_of_words = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    purpose = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user.first_name} Document"

    class Meta:
        verbose_name = "document"
        verbose_name_plural = "documents"
        db_table = "documents"
