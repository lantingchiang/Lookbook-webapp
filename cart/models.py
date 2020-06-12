from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

from decimal import Decimal

# Create your models here.
class User(AbstractUser):
    # inherit username, password, email, first_name, and last_name fields
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Products(models.Model):
    category = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    quantity = models.PositiveIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(default='Product description.')
    image_url = models.TextField(default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'


class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    products = ArrayField(models.CharField(max_length=50), default=list)
    quantities = ArrayField(models.PositiveIntegerField(), default=list)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    delivery_method = models.CharField(max_length=30, default='')
    payment_method = models.CharField(max_length=30, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'