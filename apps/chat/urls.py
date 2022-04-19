from django.urls import path

from apps.chat import views

app_name = 'chat'

urlpatterns = [
    path('<int:id>/', views.chatroom, name='chat'),
    path('load-data/<int:id>/', views.ajax_load_messages, name='chat-load-data'),
]