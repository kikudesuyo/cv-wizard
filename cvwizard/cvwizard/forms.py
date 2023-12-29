from django import forms


class UserForm(forms.Form):
    last_name = forms.CharField(label="Last Name", max_length=200)
    first_name = forms.CharField(label="First Name", max_length=200)
    birthdate = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
