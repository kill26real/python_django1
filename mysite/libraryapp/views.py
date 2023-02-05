from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
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


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = BookSerializer


    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        name = self.request.query_params.get('name')
        if author and name:
            queryset = queryset.filter(name=name, author=author)
        # pages = self.request.query_params.get('pages')
        # comparison = self.request.query_params.get('comparison')
        # if pages:
        #     if comparison == '<':
        #         queryset = queryset.filter(pages<pages)
        #     elif comparison == '>':
        #         queryset = queryset.filter(pages>pages)
        #     elif comparison == '=':
        #         queryset = queryset.filter(pages=pages)
        # TODO используйте GET параметры по аналогии с lookup для фильтрации queryset в ОRM: lt, lte, gt, gte и на
        #  основе этих значений фильтруйте: https://metanit.com/python/django/5.13.php
        #  Как вариант, есть такой удобный инструмент фильтрации:
        #  https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html#adding-a-filterset-with-filterset-class
        return queryset


    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)

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



