from django.urls import path
from .views import AuthorList, BookList, AuthorDetail, BookDetail


app_name = 'libraryappapp'
urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookList.as_view(), name='books-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]