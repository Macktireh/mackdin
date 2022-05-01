from apps.post import views
from django.urls import path

app_name = 'post'

urlpatterns = [
    path('', views.post_create_list_view, name='post_list'),
    path('post-detail/<str:uid>/', views.post_detail_view, name='post_detail'),
    # path('add-post/', views.add_post, name='add_post'),
    path('delete-post/<str:uid>/', views.delete_post, name='delete_post'),
    path('update-post/<str:uid>/', views.update_post, name='update_post'),
    path('like/', views.like_post, name='like_post'),
]