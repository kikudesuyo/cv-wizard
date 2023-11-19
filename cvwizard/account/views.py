from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import SignUpForm
from .models import AccountManagement


# Create your views here.
class SignUpView(FormView):
    def sign_up(request):
        """アカウントの新規登録"""
        if request.method == "POST":
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
                    return HttpResponse("Form is valid")
        else:
            form = SignUpForm()
        return render(request, "account/signup.html", {"form": form})
