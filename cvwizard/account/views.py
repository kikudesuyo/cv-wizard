from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import DeleteAccountForm, SignUpForm
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
                    # アカウント登録ページに移動
                    return HttpResponse("This Email already exists")
                else:
                    registration = AccountManagement(
                        username=username, password=password, email=email
                    )
                    registration.add()
                    # topページにリダイレクト
                    return HttpResponse("Form is valid")
        else:
            form = SignUpForm()
        return render(request, "account/signup.html", {"form": form})

    def delete_account(request):
        if request.method == "POST":
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
            form = DeleteAccountForm()
        return render(request, "account/delete.html", {"form": form})
