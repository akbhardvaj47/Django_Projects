from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('activate/<str:email_token>/', views.activate_account, name='activate_account'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('remove_cart/<int:cart_item_uid>/', views.remove_cart, name='remove_cart'),
    path('remove_coupon/<int:cart_uid>/', views.remove_coupon, name='remove_coupon'),
    path('update_quantity/<int:cart_item_uid>/', views.update_quantity, name='update_quantity'),
    
]
