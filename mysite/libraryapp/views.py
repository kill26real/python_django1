from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from django_filters import rest_framework as filters


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка авторов, а также создания новых"""
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        author_name = self.request.query_params.get('name')
        if author_name:
            queryset = queryset.filter(name=author_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class AuthorDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации, обновления и удаления"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookFilter(filters.FilterSet):
    min_pages = filters.NumberFilter(field_name="pages", lookup_expr='gte')
    max_pages = filters.NumberFilter(field_name="pages", lookup_expr='lte')
    pages = filters.NumberFilter(field_name="pages")

    class Meta:
        model = Book
        fields = ['name', 'author', 'pages']


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка книг, а также создания новых"""
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter


    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        name = self.request.query_params.get('name')
        if author and name:
            queryset = queryset.filter(name=name, author=author)
        return queryset


    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации, обновления и удаления"""
    queryset = Book.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class AuthorList(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request, format=None):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class BookList(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request, format=None):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)



