from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.friends.models import Relationship


class RelationshipAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('date_created', 'sender', 'receiver', 'status', 'date_sender', 'date_receiver',)
    list_filter = ('status', 'date_sender', 'date_receiver',)
    list_editable = ('status',)
    ordering = ('-date_created',)
    list_per_page = 20
    list_max_show_all = 200

    # def name(self, obj):
    #     return obj.sender


admin.site.register(Relationship, RelationshipAdmin)
