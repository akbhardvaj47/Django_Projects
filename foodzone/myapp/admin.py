from django.contrib import admin
from myapp.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'added_on', 'is_approved')
    list_filter = ('is_approved', 'added_on')  # Filter by approval status and date
    search_fields = ('name', 'email', 'subject')  # Search by these fields
    ordering = ('-added_on',)  # Order by the most recent first

admin.site.register(Contact, ContactAdmin)
