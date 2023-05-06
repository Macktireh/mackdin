from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.users.models import CustomUser

admin.site.site_header = "Social Network Mackdin"
admin.site.site_title = "Interface Administrateur"
admin.site.index_title = "Mackdin"

class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_email_verified', 'is_staff', 'is_superuser', 'date_joined',)
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_email_verified', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_email_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('date_joined', 'last_login', 'last_logout',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_active', 'is_email_verified', 'is_staff')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('-date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)