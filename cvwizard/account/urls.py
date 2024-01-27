from django.urls import include, path

from . import views

urlpatterns = [
    path("account/top", views.TopView.as_view(), name="top"),
    path("account/signup", views.SignUpView.as_view(), name="signup"),
    path("account/login", views.LoginView.as_view(), name="login"),
    path("", views.ProfileView.as_view(), name="profile"),
]
