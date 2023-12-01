from django.urls import include, path

from . import views

urlpatterns = [
    path("account/signup", views.SignUpView.as_view(), name="signup"),
    path("account/login", views.LoginView.as_view(), name="login"),
    path("account/delete", views.DeleteAccountView.as_view(), name="delete"),
]
