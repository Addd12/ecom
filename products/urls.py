from django.urls import path
from .views import ProductDetailView, ProductUpdateView, ProductDeleteView


urlpatterns = [
    #path('', ProductListView.as_view(), name='products'),
    path('product-details/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('edit-product/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
]
