from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.comments.models import Comment, ReponseComment, LikeComment


class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Author_comment', 'post', 'message', 'count_like', 'date_added',)

    ordering = ('-date_added',)
    
    def Author_comment(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
    def count_like(self, obj):
        return f"{obj.liked.all().count()}"
    
admin.site.register(Comment, CommentAdmin)

class ReponseCommentAdmin(admin.ModelAdmin):
    list_display = ('Author_comment_reponse', 'comment', 'message', 'date_added',)

    ordering = ('-date_added',)
    
    def Author_comment_reponse(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
admin.site.register(ReponseComment, ReponseCommentAdmin)


class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'comment', 'value',)
    
    def user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    # def post_id(self, obj):
    #     return f"{obj.comment.id}"
    
admin.site.register(LikeComment, LikeCommentAdmin)
