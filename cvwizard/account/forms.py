from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        max_length=200,
        help_text="有効なメールアドレスを入力してください。",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email", max_length=200)
    password = forms.CharField(label="password", max_length=200)


class ChangePasswordForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=200)


class DeleteAccountForm(forms.Form):
    password = forms.CharField(label="Password", max_length=200)
