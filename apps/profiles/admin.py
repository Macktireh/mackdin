from django.contrib import admin
from apps.profiles.models import Profile  
from django.utils.translation import gettext_lazy as _

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pseudo', 'bio', 'birth_date', 'gender', 'phone', 'adress', 'town', 'country', 'number_views',)
    # list_filter = ('gender',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        
        (_('Personal info'), {'fields': ('pseudo', 'bio', 'img_profile', 'img_bg', 'birth_date', 'gender', 'phone',)}),
        
        (_('Location'), {'fields': ('adress', 'town', 'region', 'zipcode', 'country',),}),
        # (_('User description'), {'fields': ('description', 'bio')}),
        
        (_('Description'), {'fields': ('description',)}),
        (_('Social network'), {'fields': ('link_linkedin', 'link_gitthub', 'link_twitter', 'link_mysite',)}),
        (_('Friends'), {'fields': ('friends',)}),
    )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_active', 'is_email_verified', 'is_staff')}
    #     ),
    # )
    search_fields = ('pseudo', 'gender', 'town', 'country',)
    ordering = ('-date_updated',)
    
    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
admin.site.register(Profile, ProfileAdmin)
