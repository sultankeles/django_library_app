from django.contrib import admin

from .models import Categories, Books

admin.site.register(Categories)
admin.site.register(Books)