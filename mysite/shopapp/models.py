from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    class Meta:
        ordering = ['name', 'price']

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archivated = models.BooleanField(default=False)

    def __str__(self):
        return f'Product(pk={self.pk}, name={self.name!r}'

class Order(models.Model):
    delivery_adress = models.TextField(null=False, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=True)


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=True)


class Shop(models.Model):
    name = models.CharField(max_length=100)
    adress = models.TextField(null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    products = models.ManyToManyField(Product, related_name='shops')