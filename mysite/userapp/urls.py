from django.urls import path
from .views import MyLoginView, MyLogoutView, register_view

app_name = 'userapp'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]