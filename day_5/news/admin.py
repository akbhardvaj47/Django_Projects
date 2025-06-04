from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):  # Capitalize 'N' to follow naming conventions
    list_display = ('news_title', 'news_desc')  # List fields you want to display

admin.site.register(News, NewsAdmin)  # Register News model with NewsAdmin class
