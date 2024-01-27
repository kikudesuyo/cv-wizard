from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import LoginForm, SignUpForm


# Create your views here.
class TopView(TemplateView):
    def get(self, request):
        return render(request, "account/top.html")


class SignUpView(CreateView):
    template_name = "account/signup.html"
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
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
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username="aaa", email=email, password=password)
            if user is not None:
                return HttpResponse("Successfully logg in")
            return HttpResponse("failed...")


class ProfileView(TemplateView):
    template_name = "account/profile.html"
