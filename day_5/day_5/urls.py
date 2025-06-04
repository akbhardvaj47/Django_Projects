from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from day_5 import views  # Assuming views are defined in day_5/views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('projects/', views.projects_page, name='projects'),
    path('contact/', views.contact_page, name='contact'),
    path('skills/', views.skills_page, name='skills'),
    path('news_details/<int:news_id>/', views.news_details, name='news_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
