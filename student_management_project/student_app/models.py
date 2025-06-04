from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    added_on = models.DateTimeField(auto_now_add=True)
     

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
     
    class Meta:
        verbose_name_plural='Student Table'

