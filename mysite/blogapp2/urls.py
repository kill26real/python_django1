from django.urls import path
from .views import ArticlesListView, ArticleDetailsView, ArticleCreateView, ArticleUpdateView, LoginErrorView

app_name = 'blogapp2'

urlpatterns = [
    path('', ArticlesListView.as_view(), name='articles-list'),
    path('<int:pk>/', ArticleDetailsView.as_view(), name='article-details'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('login_error/', LoginErrorView.as_view(), name='login-error'),
]
