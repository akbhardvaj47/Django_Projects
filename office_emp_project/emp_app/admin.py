from django.contrib import admin

# Register your models here.
from .models import Employee, Role, Department

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)