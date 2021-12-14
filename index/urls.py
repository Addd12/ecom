from django.urls import path
from .views import *
from products.views import ProductListView



urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    #path("", index, name="index")
]