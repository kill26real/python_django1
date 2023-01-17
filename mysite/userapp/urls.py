from django.urls import path
from .views import login_view, AnotherLoginView, logout_view, AnotherLogoutView

app_name = 'userapp'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('logout/', logout_view, name='logout'),
]