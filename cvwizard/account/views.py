from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import DeleteAccountForm, LoginForm, SignUpForm
from .models import AccountManagement


# Create your views here.
class TopView(TemplateView):
    def get(self, request):
        return render(request, "account/top.html")


class SignUpView(CreateView):
    template_name = "account/signup.html"
    form_class = SignUpForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request, "account/top.html")

    def form_invalid(self, form):
        return super().form_invalid(form)


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


class ProfileView(TemplateView):
    template_name = "account/profile.html"


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
