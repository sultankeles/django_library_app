from rest_framework import serializers

from .models import Categories, Books


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = (
            'id',
            'category',
        )


class BooksSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField() # read only

    class Meta:
        model = Books
        fields = (
            'id',
            'title',
            'author',
            'category',
            'release_date',
            'pages',
            'country',
            'language',
        )