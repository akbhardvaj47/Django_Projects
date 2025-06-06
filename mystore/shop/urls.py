from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [  
    path('', views.index, name='shopHome' ),
    path('about/', views.about, name='about' ),
    path('contact/', views.contact, name='contact' ),
    path('tracker/', views.tracker, name='tracker' ),
    path('product/', views.productView, name='productView' ),
    path('search/', views.search, name='search' ),
    path('checkout/', views.checkout, name='checkout' ),
]
