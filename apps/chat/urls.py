from django.urls import path

from apps.chat import views

app_name = 'chats'

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('chatroom/<str:uid>/', views.chatroom, name='chatroom'),
    path('load-data/<str:uid>/', views.ajax_load_messages, name='chat-load-data'),
    path('chat-api-notif/', views.chat_api_view, name='chat-api-notif'),
]