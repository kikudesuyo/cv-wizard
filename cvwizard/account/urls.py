from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("account/signup", views.SignUpView.as_view(), name="signup"),
    path("account/login", views.LoginView.as_view(), name="login"),
    path("", views.ProfileView.as_view(), name="profile"),
    path("account/delete", views.DeleteAccountView.as_view(), name="delete"),
]
