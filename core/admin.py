from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'short_message']
    search_fields = ['subject', 'email', 'short_message', 'id', 'name']

    def short_message(self, obj):
        msg = obj.message
        if len(msg) < 40:
            return msg
        elif len(msg) >= 40:
            return msg[:40] + '...'
