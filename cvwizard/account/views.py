from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import DeleteAccountForm, LoginForm, SignUpForm
from .models import AccountManagement


# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "account/signup.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            if AccountManagement.objects.filter(email=email).exists():
                return HttpResponse("This Email already exists")
            else:
                registration = AccountManagement(
                    username=username, password=password, email=email
                )
                registration.add()
                # topページにリダイレクト
                return HttpResponse("Form is valid")
        else:
            return HttpResponse("Form is invalid")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "account/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]
            if (
                AccountManagement.objects.filter(username=username_or_email).exists()
                or AccountManagement.objects.filter(email=username_or_email).exists()
            ):
                if AccountManagement.objects.filter(password=password).exists():
                    return HttpResponse("Successfully logged in")
                else:
                    # ログインページに移動
                    return HttpResponse("Password is not correct")
            else:
                # アカウント削除ページに移動
                return HttpResponse("Password is not correct")


class DeleteAccountView(View):
    def get(self, request):
        form = DeleteAccountForm()
        return render(request, "account/delete.html", {"form": form})

    def post(self, request):
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            if AccountManagement.objects.filter(password=password).exists():
                deletion = AccountManagement.objects.filter(password=password)
                deletion.delete()
                # topページにリダイレクト
                return HttpResponse("Successfully deleted")
            else:
                # アカウント削除ページに移動
                return HttpResponse("Password is not correct")
        else:
            return HttpResponse("Form is invalid")
