from django.urls import include, path

from . import views

urlpatterns = [
    path("account/signup", views.SignUpView.sign_up, name="signup"),
]
