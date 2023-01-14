from timeit import default_timer
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import Group
from .models import Product, Order
from .forms import ProductForm, OrderForm


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 100),
        ('Phone', 200),
        ('TV', 300)
    ]
    context = {
        'products': products,
        'time_running': default_timer
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)


def create_product(request: HttpRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # Product.objects.create(**form.cleaned_data)
            form.save()
            url = reverse('shopapp:products-list')
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'shopapp/create-product.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)


def create_order(request: HttpRequest):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            Order.objects.create(**form.cleaned_data)
            # form.save()
            url = reverse('shopapp:orders-list')
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        'form': form,
    }
    return render(request, 'shopapp/create-order.html', context=context)
