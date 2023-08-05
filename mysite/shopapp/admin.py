from django.contrib import admin
from django.shortcuts import render, redirect

from .common import save_csv_products
from .models import Product, Order, Sale, Offer, Shop
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from .admin_mixins import ExportAsCSVMixin
from .forms import  CSVImportForm
from django.urls import path


class ProductShopInline(admin.StackedInline):
    model = Shop.products.through


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [
        ProductShopInline,
    ]
    list_display = ['name', 'adress', 'description']


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description='Archive products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archivated=True)


@admin.action(description='Unarchive products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archivated=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    change_list_template = 'shopapp/products_changelist.html'

    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',
    ]
    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'name', 'description_short', 'price', 'discount', 'archivated'
    list_display_links = 'pk', 'name'
    ordering = ['name', 'pk']
    search_fields = ['name', 'description']
    fieldsets = [
        (None, {
            'fields': ('name', 'description')
        }),
        ('Price options', {
            'fields': ('price', 'discount'),
            'classes': ('collapse', 'wide'),
        }),
        ('Extra options', {
            'fields': ('archivated',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archivated" is for soft delete'
        })
    ]

    def description_short(self, obj: Product):
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'

    def import_csv(self, request: HttpRequest) -> HttpResponse:
        if request.method == 'GET':
            form = CSVImportForm()
            context = {
                'form': form,
            }
            return render(request, 'admin/csv_form.html', context)
        form = CSVImportForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                'form': form,
            }
            return render(request, 'admin/csv_form.html', context, status=400)

        save_csv_products(
            form.files['csv_file'].file,
            encoding=request.encoding,
        )

        self.message_user(request, 'Data from CSV was imported')
        return redirect('..')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(
                'import-products-csv/',
                self.import_csv,
                name='import_products_csv',
            ),
        ]
        return new_urls + urls


class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'delivery_adress', 'promocode', 'created_at', 'user_verbose'

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order):
        return obj.user.first_name or obj.user.username

