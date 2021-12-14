from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products')
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})