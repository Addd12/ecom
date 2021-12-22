from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products')
    description = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('product-details', kwargs={'pk': self.pk})