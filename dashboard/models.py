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

class content_artices_model(models.Model):
    class textChoices(models.TextChoices):
        Blog_content = "Blog content"
        Content_write = "Content write"
        News_content = "News content"
        Scientific_content = "Scientific content"
        Educational_content = "Educational content"
        Other = "Other"
        
    type = models.CharField(max_length=50, choices=textChoices.choices)
    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="articles/images", blank=True, null=True)


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"
        db_table = "articles"



        