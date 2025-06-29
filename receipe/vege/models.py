from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=100)
    recipe_desc=models.TextField(max_length=300)
    recipe_image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.recipe_name