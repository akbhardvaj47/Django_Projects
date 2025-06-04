from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ✅ Directly reference the view
]
