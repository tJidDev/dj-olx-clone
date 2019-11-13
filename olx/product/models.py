from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#
class Product(models.Model):
    CONDITION   =   (('new','New'),('used','Used'))
    title       =   models.CharField(max_length=100)
    owner       =   models.ForeignKey(User, on_delete=models.CASCADE)
    description =   models.TextField(max_length=500)
    condition   =   models.CharField(max_length=100, choices=CONDITION)
    category    =   models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand    =   models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    price       =   models.DecimalField(max_digits=9, decimal_places=2)
    created     =   models.DateTimeField(default=timezone.now)
    updated     =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product =   models.ForeignKey(Product, on_delete=models.CASCADE)
    image   =   models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name_plural =   'Product Images'

    def __str__(self):
        return self.product.title


class Category(models.Model):
    name    =   models.CharField(max_length=50)
    icon   =   models.CharField(max_length=50, blank=True, null=True)
    color    =   models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =   'categories'


class Brand(models.Model):
    name    =   models.CharField(max_length=50)

    def __str__(self):
        return self.name
