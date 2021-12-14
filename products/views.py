from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'index/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'description', 'image', 'price']

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'