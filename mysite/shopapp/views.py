from timeit import default_timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import Group
from.models import Product, Order

def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 100),
        ('Phone', 200),
        ('TV', 300)
    ]
    context = {
        'products':products,
        'time_running':default_timer
    }
    return render(request, 'shopapp/shop-index.html', context=context)

def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)

def products_list(request: HttpRequest):
    context = {
        'products':Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)

def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)
