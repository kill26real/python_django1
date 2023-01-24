from django.urls import path
from .views import MyLoginView, MyLogoutView, register_view, AccountView, AccountUpdateView

app_name = 'userapp'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('<int:pk>/', AccountView.as_view(), name='account'),
    path('<int:pk>/update/', AccountUpdateView.as_view(), name='account_update'),
]