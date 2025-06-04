
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name='home'),
    path('add-student', views.add_student, name='add_student'), 
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    # path('student-list/', views.student_list, name='student_list'),
]
