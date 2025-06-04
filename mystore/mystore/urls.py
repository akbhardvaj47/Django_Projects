from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),       # Route for the Django admin interface
    path('shop/', include('shop.urls')),   # Route prefix for the 'shop' app
    path('blog/', include('blog.urls')),   # Route prefix for the 'blog' app
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)