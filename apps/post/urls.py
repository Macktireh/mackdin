from apps.post import views
from django.urls import path

app_name = 'post'

urlpatterns = [
    path('', views.post_create_list_view, name='post_list'),
    path('<int:post_id>/', views.post_detail_view, name='post_detail'),
    # path('add-post/', views.add_post, name='add_post'),
    path('<int:post_id>/delete-post/', views.delete_post, name='delete_post'),
    path('<int:post_id>/update-post/', views.update_post, name='update_post'),
    path('like/', views.like_post, name='like_post'),
]