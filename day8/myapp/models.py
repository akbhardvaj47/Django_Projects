from django.db import models

# Create your models here.
class Brand(models.Model):
    # product_id=models.AutoField()
    product_name=models.CharField(max_length=50)
    product_desc=models.TextField(max_length=300)

    def __str__(self):
        return self.product_name