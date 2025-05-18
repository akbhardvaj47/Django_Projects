"""
URL configuration for foodzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodzone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name='home_page'),
    path('about/', views.about_page,name='about_page'),
    path('feature/', views.feature_page,name='feature_page'),
    path('team/', views.team_page,name='team_page'),
    path('menu/', views.menu_page,name='menu_page'),
    path('booking/', views.booking_page,name='booking_page'),
    path('contact/', views.contact_page,name='contact_page'),
    path('single/', views.single_page,name='single_page'),
    path('blog/', views.blog_page,name='blog_page'),
]
