from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"style": "border: 1px solid black"}),
            "email": forms.EmailInput(attrs={"style": "border: 1px solid black"}),
            "message": forms.Textarea(
                attrs={"style": "border: 1px solid black", "rows": 22}
            ),
        }
