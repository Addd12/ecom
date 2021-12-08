from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path("register/", register, name="register"), #it was "/register" and it couldn't find the path so careful!
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name="login")
]
