from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default='')
    sub_category = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
