from django.urls import path
from .views import MyLoginView, MyLogoutView, register_view, AccountView, ProfileUpdateView, UserUpdateView

app_name = 'userapp'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('<int:pk>/', AccountView.as_view(), name='account'),
    path('<int:pk>/update_profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('<int:pk>/update_user/', UserUpdateView.as_view(), name='user_update'),
]