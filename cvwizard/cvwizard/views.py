from django.http import Http404, HttpResponse
from django.shortcuts import render

from .forms import UserForm
from .models import User


# Create your views here.
def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            birthdate = form.cleaned_data["birthdate"]
            user = User(name=name, birthdate=birthdate)
            user.save()
            return HttpResponse("Form is valid")
    else:
        form = UserForm()
    return render(request, "cvwizard/index.html", {"form": form})


def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, "cvwizard/detail.html", {"user": user})
