from django.urls import path
from .views import *


urlpatterns = [
    path("register/", register, name="register") #it was "/register" and it couldn't find the path so careful!
]
