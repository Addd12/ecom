from django.urls import path
from .views import ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView, ProductListView


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-details'),
    path('product/new/', ProductCreateView.as_view(), name='new-product'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
]
