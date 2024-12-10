from django.contrib import admin
from .models import (
    humanized_texts_model,
    saved_documents,
    content_artices_model,
    Billing_model,
)

admin.site.register(humanized_texts_model)
admin.site.register(saved_documents)
admin.site.register(content_artices_model)


@admin.register(Billing_model)
class BillingAdmin(admin.ModelAdmin):
    list_display = ["user", "how_much", "type", "paid_date", "expire_date"]
    list_filter = ["user", "paid_date", "type"]
    readonly_fields = ["expire_date"]
