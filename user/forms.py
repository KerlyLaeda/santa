from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
    #     self.fields["first_name"].widget.attrs.update({"class": "form-control"})
    #     self.fields["last_name"].widget.attrs.update({"class": "form-control"})
    #     self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "email@example.com"})
    #     self.fields["password1"].widget.attrs.update({"class": "form-control"})
    #     self.fields["password2"].widget.attrs.update({"class": "form-control"})
    # for field in self.fields.values():
    #   field.widget.attrs["class"] = "form-control"
