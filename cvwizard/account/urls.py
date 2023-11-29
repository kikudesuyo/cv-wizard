from django.urls import include, path

from . import views

urlpatterns = [
    path("account/signup", views.SignUpView.as_view(), name="signup"),
    path("account/delete", views.DeleteAccountView.as_view(), name="delete"),
]
