from django.contrib import admin
from .models import humanized_texts_model, saved_documents

admin.site.register(humanized_texts_model)
admin.site.register(saved_documents)
