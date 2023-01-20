from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, NewsDeleteView

app_name = 'newsapp'
urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-details'),
    path('create/', NewsCreateView.as_view(), name='news-create'),
]