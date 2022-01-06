from django.db import models
from django.db.models import fields
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Product
from django.contrib.auth.models import User


# def home(request):
#     context = {
#         'products': Product.objects.all()  
#     }
#     return render(request, 'index/index.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'index/index.html'
    context_object_name = 'products'
    ordering = ['-date_posted']

    # def get_queryset(self):
    #     user = get_object_or_404(User, username = self.kwargs.get('username'))
    #     return Product.objects.filter(owner=user)

class ProductDetailView(DetailView):
    model = Product

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'image', 'price']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.owner:
            return True
        return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/' #redirects to home page after the item is deleted

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.owner:
            return True
        return False

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'description', 'image', 'price']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
