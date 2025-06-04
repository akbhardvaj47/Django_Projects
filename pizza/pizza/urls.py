
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('home.urls')),
    path('', home, name='home'),
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('cart/', cart, name='cart_page'),
    path('order/', order, name='order_page'),
    path('checkout/', checkout, name='checkout_page'),
    path('remove-cart-item/<cart_item_uid>/', remove_cart_items, name='remove_cart_items'),
    path('add-cart/<pizza_uid>', add_cart, name='add_cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)