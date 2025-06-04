from django.db import models
# Create your models here.

class Project(models.Model):
    # file will be uploaded to MEDIA_ROOT / img 
    project_img = models.ImageField(upload_to ='img/')
    project_name=models.CharField(max_length=50)
    project_desc=models.TextField(max_length=200)