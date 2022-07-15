from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.notifications.models import Notification

class NotificationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('date_created', 'type_notif', 'from_user', 'to_user', 'seen', 'bg_seen',)
    list_editable = ('type_notif', 'seen', 'bg_seen',)
    list_filter = ('type_notif', 'seen', 'bg_seen',)
    ordering = ('-date_created',)

admin.site.register(Notification, NotificationAdmin)