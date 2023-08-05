from django.urls import path
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductsDetailsView,
    ProductsListView,
    OrdersListView,
    OrderDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OrderUpdateView,
    OrderCreateView,
    OrderDeleteView,
    LatestProductsFeed,
)

app_name = 'shopapp'
urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('groups/', GroupsListView.as_view(), name='groups-list'),
    path('products/', ProductsListView.as_view(), name='products-list'),
    path('products/latest/feed/', LatestProductsFeed(), name='products-feed'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductsDetailsView.as_view(), name='product-details'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/archive/', ProductDeleteView.as_view(), name='product-delete'),
    path('orders/', OrdersListView.as_view(), name='orders-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order-details'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
]
