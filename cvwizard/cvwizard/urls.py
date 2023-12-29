from django.urls import path

from . import views

urlpatterns = [
    path("cvwizard/", views.index, name="index"),
    path("cvwizard/view_users/", views.view_users, name="view_users"),
]
