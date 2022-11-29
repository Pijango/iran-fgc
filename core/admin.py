from django.contrib import admin
from .models import Contact, Workshop


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'short_message', 'date']
    search_fields = ['subject', 'email', 'short_message', 'id', 'name', 'date']

    def short_message(self, obj):
        msg = obj.message
        if len(msg) < 40:
            return msg
        elif len(msg) >= 40:
            return msg[:40] + '...'


@admin.register(Workshop)
class Workshop(admin.ModelAdmin):
    pass
