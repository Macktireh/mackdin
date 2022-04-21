from django.urls import path

from apps.chat import views

app_name = 'chats'

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('<int:id>/', views.chatroom, name='chatroom'),
    path('load-data/<int:id>/', views.ajax_load_messages, name='chat-load-data'),
    path('chat-api-notif/', views.chat_api_view, name='chat-api-notif'),
]