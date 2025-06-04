
from django.contrib import admin
from django.urls import path
from testing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),  # Home page URL
    path('project_details/<slug:slug>/', views.project_details, name='project_details'),
]
