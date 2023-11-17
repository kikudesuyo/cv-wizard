from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm
from .models import User

# Create your views here.
def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            first_name = form.cleaned_data["first_name"]
            birthdate = form.cleaned_data["birthdate"]
            user = User(last_name=last_name, first_name=first_name, birthdate=birthdate)
            user.save()
            return HttpResponse("Form is valid")
    else:
        form = UserForm()
    return render(request, "cvwizard/index.html", {"form": form})


def view_users(request):
    data_from_db = User.objects.values()
    data_attr = [field.name for field in User._meta.get_fields()]
    return render(request, "cvwizard/view_users.html", {"data_from_db": data_from_db, "data_attr": data_attr})
