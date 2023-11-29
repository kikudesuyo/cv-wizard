from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import UserForm
from .models import User


# Create your views here.
class FormView(View):
    form_class = UserForm
    template_name = "cvwizard/index.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            first_name = form.cleaned_data["first_name"]
            birthdate = form.cleaned_data["birthdate"]
            user = User(last_name=last_name, first_name=first_name, birthdate=birthdate)
            user.add()
            return HttpResponse("Form is valid")
        return render(request, self.template_name, {"form": form})


class DatabaseView(View):
    template_name = "cvwizard/view_users.html"

    def get(self, request):
        data_from_db = User.objects.values()
        data_attr = [field.name for field in User._meta.get_fields()]
        return render(
            request,
            self.template_name,
            {"data_from_db": data_from_db, "data_attr": data_attr},
        )
