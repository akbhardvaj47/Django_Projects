from django.contrib import admin
from .models import News

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_desc')

admin.site.register(News, ProjectAdmin)
