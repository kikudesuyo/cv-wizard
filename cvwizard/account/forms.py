from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=200)
    password = forms.CharField(label="Password", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)


class ChangePasswordForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=200)


class DeleteAccountForm(forms.Form):
    password = forms.CharField(label="Password", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
