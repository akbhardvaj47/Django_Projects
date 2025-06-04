from django.contrib import admin
from student_app.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','email','address','phone','added_on')

admin.site.register(Student,StudentAdmin)    