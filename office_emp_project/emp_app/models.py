from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Role(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self):
        return f'{self.first_name}'

