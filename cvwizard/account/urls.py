from django.urls import include, path

from . import views

urlpatterns = [
    path("account/signup", views.SignUpView.sign_up, name="signup"),
    path("account/delete", views.SignUpView.delete_account, name="delete"),
]
