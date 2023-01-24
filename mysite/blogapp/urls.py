from django.urls import path
from .views import PostsListView, LoginErrorView, PostDetailView, upload_post, create_post

app_name = 'blogapp'
urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('login-error/', LoginErrorView.as_view(), name='login_error'),
    path('create/', create_post, name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-details'),
    path('upload_posts/', upload_post, name='upload-posts'),
]