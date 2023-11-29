from django.urls import path

from . import views

urlpatterns = [
    path("cvwizard/", views.FormView.as_view(), name="index"),
    path("cvwizard/view_users/", views.DatabaseView.as_view(), name="view_users"),
]
