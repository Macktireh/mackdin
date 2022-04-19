from django.contrib import admin

from apps.chat.models import Messenger

class MessengerAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'sender', 'reciever', 'message', 'seen',)
    list_editable = ('sender', 'reciever', 'seen',)
    list_filter = ('seen', 'date_created',)

admin.site.register(Messenger, MessengerAdmin)
