from timeit import default_timer
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Order
from .forms import ProductForm, OrderForm, GroupForm


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
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

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': GroupForm,
            'groups': Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)


    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    queryset = Product.objects.filter(archivated=False)
    context_object_name = 'products'


class ProductsDetailsView(DetailView):
    template_name = 'shopapp/product-details.html'
    model = Product
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shopapp:products-list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = 'name', 'price', 'description', 'discount'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shopapp:product-details',
            kwargs={'pk': self.object.pk},
        )

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products-list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archivated = True
        self.object.save()
        return HttpResponseRedirect(success_url)



class OrdersListView(ListView):
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )


class OrderDetailView(DetailView):
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )


class OrderUpdateView(UpdateView):
    model = Order
    fields = 'user', 'delivery_adress', 'promocode', 'products'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shopapp:order-details',
            kwargs={'pk': self.object.pk},
        )


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('shopapp:orders-list')


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('shopapp:orders-list')


# def create_order(request: HttpRequest):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             products = form.cleaned_data['products']
#             instance = form.save()
#             instance.products.add(*form.cleaned_data['products'])
#             url = reverse('shopapp:orders-list')
#             return redirect(url)
#     else:
#         form = OrderForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'shopapp/order_form.html', context=context)
