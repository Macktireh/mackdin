from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.chat.models import Messenger

class MessengerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('date_created', 'sender', 'reciever', 'message', 'seen',)
    list_editable = ('seen',)
    list_filter = ('seen', 'date_created',)

admin.site.register(Messenger, MessengerAdmin)
