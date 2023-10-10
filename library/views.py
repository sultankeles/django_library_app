from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Categories, Books
from .serializers import CategoriesSerializer, BooksSerializer


class CategoriesMVS(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class BooksMVS(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer