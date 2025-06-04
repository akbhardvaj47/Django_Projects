"""
URL configuration for mydjango project.

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
from mydjango import views  #we have to import the file from which we want to call functions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),  # Added name for better URL referencing
    path('about-me/', views.aboutMe, name='about_me'),
    path('contact-me/', views.contact, name='contact_me'),  
    path('intro/', views.intro, name='intro'),
    path('course/', views.course, name='course'),
    path('card/', views.card, name='card'),
    path('course/<int:courseId>/', views.courseDetails, name='course_details'),
]
