
from django.contrib import admin
from django.urls import path,include
from vege.views import recipe


urlpatterns = [
    path('',recipe, name='index_page')
]
