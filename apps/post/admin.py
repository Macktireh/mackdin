from django.contrib import admin
from apps.post.models import Post, LikePost
from django.utils.translation import gettext_lazy as _

class PostAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'message', 'number_of_like', 'number_of_comment', 'date_created',)

    ordering = ('-date_created',)
    
    def full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
    def number_of_like(self, obj):
        return f"{obj.liked.all().count()}"
    
    def number_of_comment(self, obj):
        return f"{obj.post_comment.all().count()}"
    
admin.site.register(Post, PostAdmin)

class LikePostAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post_id', 'value',)
    
    def user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def post_id(self, obj):
        return f"{obj.post.id}"
    
admin.site.register(LikePost, LikePostAdmin)
