from django.urls import path

from . import views

urlpatterns = [
    path("cvwizard/", views.index, name="index"),
]
