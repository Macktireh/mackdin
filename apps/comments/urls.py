from django.urls import path
from apps.comments import views

app_name = 'comments'

urlpatterns = [
    # path('api-data/', views.comment_all_data, name='api-comment'),
    path('post/<str:post_id>/', views.get_comments_post, name='get-comment-post'),
    path('add-update-comment/', views.add_update_comment_view, name='add-update-comment'),
    path('delete-comment/', views.delete_comment, name='delete-comment'),
]