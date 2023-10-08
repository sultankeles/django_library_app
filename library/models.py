from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.ManyToManyField(Categories, related_name='books')
    release_date = models.DateField()
    pages = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=20)
    language = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title} - {self.author}'