from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    category_image = models.ImageField(upload_to='categories')

    def save(self, *args, **kwargs):
        if not self.slug:  # Agar slug empty hai (if not self.slug:),
            self.slug = slugify(self.category_name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class ColorVariant(BaseModel):
    color_name=models.CharField(max_length=100,)
    price=models.IntegerField(default=0)

    def __str__(self):
      return self.color_name

class SizeVariant(BaseModel):
    size_name=models.CharField(max_length=100,)
    price=models.IntegerField(default=0)
        
    def __str__(self):
       return self.size_name    

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=
                               models.CASCADE, related_name='products')  
    image=models.ImageField(upload_to='product')  
    price=models.IntegerField()
    product_desc=models.TextField(max_length=300)
    color_variant=models.ManyToManyField(ColorVariant,blank=True)
    size_variant=models.ManyToManyField(SizeVariant,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Agar slug empty hai (if not self.slug:),
            self.slug = slugify(self.product_name)
        return super(Product, self).save(*args, **kwargs)
    
    def get_product_price_by_size(self, size_name):
        try:
            size_obj = self.size_variant.get(size_name=size_name)
            return self.price + size_obj.price
        except SizeVariant.DoesNotExist:
            return self.price

    def get_product_price_by_color(self, color_name):
        try:
            color_obj=self.color_variant.get(color_name=color_name)  
            return self.price+color_obj.price
        except ColorVariant.DoesNotExist:
            return self.price   

     
    def get_updated_price(self, size_name=None, color_name=None):
        final_price = self.price

        if size_name:
            size_obj = self.size_variant.filter(size_name=size_name).first()
            if size_obj:
                final_price += size_obj.price

        if color_name:
            color_obj = self.color_variant.filter(color_name=color_name).first()
            if color_obj:
                final_price += color_obj.price

        return final_price


    def __str__(self):
        return self.product_name
    


class ProductImage(BaseModel):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images') 
    image=models.ImageField(upload_to='product')   


class Coupon(BaseModel):
    coupon_code=models.CharField(max_length=10)
    is_expired=models.BooleanField(default=False)
    discount_price=models.IntegerField(default=100)
    minimum_order=models.IntegerField(default=500)
