from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, ListView

from .forms import UserForm
from .models import User


# Create your views here.
class FormView(FormView):
    form_class = UserForm
    template_name = "cvwizard/index.html"

    def form_valid(self, form):
        form.save()
        return HttpResponse("Form is valid")


class DatabaseView(ListView):
    template_name = "cvwizard/view_users.html"

    def get(self, request):
        data_from_db = User.objects.values()
        data_attr = [field.name for field in User._meta.get_fields()]
        return render(
            request,
            self.template_name,
            {"data_from_db": data_from_db, "data_attr": data_attr},
        )
