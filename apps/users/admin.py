from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_email_verified', 'is_staff', 'is_superuser', 'date_joined',)
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_email_verified', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_email_verified', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
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