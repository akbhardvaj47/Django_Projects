
from django.contrib import admin
from django.urls import path
from student_management_project.views import home_page, delete_student, edit_student, update_student,add_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page,name='home'),
    path('add-student', add_student, name='add_student'), 
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
    path('edit/<int:student_id>/', edit_student, name='edit_student'),
    path('update/<int:student_id>/', update_student, name='update_student'),
    # path('student-list/', views.student_list, name='student_list'),
]
