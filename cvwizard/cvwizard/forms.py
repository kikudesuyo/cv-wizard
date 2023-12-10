from datetime import date

from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "birthdate"]
        widgets = {"birthdate": forms.DateInput(attrs={"type": "date"})}

    def is_valid(self):
        super().is_valid()
        if self.cleaned_data["birthdate"] > date.today():
            raise ValueError("Birthdate cannot be in the future")
