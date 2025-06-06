from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True

class PizzaCategory(BaseModel):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Pizza(BaseModel):
    category=models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name='category')
    pizza_name=models.CharField(max_length=100)
    price=models.IntegerField(default=100)
    image=models.ImageField(upload_to='pizza')
    description = models.TextField(blank=True, null=True)
    discount = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.pizza_name


class Cart(BaseModel):
    user=models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL, related_name='carts')
    is_paid=models.BooleanField(default=False) 
        
    def get_cart_total(self):
        total = 0
        for item in self.cart_items.all():
            total += item.pizza.price * item.quantity
        return total


class CartItems(BaseModel):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
                  
