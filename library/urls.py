from django.urls import path, include

from .views import CategoriesMVS, BooksMVS

from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoriesMVS)
router.register('books', BooksMVS)


urlpatterns = [
    path('', include(router.urls)),    
]