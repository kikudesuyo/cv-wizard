from django import forms

from .models import User


class UserForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    birthdate = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
