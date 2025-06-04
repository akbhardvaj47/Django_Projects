# home/urls.py
from django.urls import path
from home.views import index, search

urlpatterns = [
    path('', index, name='index'),
    path('products/search/', search, name='search'),
]