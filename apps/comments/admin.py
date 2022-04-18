from django.contrib import admin
from apps.comments.models import Comment, ReponseComment, LikeComment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'message', 'count_like', 'date_added',)

    ordering = ('-date_added',)
    
    def full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
    def count_like(self, obj):
        return f"{obj.liked.all().count()}"
    
admin.site.register(Comment, CommentAdmin)

class ReponseCommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'comment', 'message', 'date_added',)

    ordering = ('-date_added',)
    
    def full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
admin.site.register(ReponseComment, ReponseCommentAdmin)


class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'comment', 'value',)
    
    def user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    # def post_id(self, obj):
    #     return f"{obj.comment.id}"
    
admin.site.register(LikeComment, LikeCommentAdmin)
