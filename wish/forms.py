from django import forms
from .models import Wish


class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ["wish"]
        widgets = {
            "wish": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Write your wish here..."
            }),
        }
