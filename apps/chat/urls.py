from django.urls import path

from apps.chat import views


urlpatterns = [
    path('<int:id>/', views.chatroom, name='chat')
]