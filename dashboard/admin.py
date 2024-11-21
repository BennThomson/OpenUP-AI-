from django.contrib import admin
from .models import humanized_texts_model, saved_documents, content_artices_model

admin.site.register(humanized_texts_model)
admin.site.register(saved_documents)
admin.site.register(content_artices_model)
