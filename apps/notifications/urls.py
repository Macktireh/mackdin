from apps.notifications import views
from django.urls import path

app_name = 'notifications'

urlpatterns = [
    path('', views.list_notification, name='notif'),
    path('<int:id>/seen/', views.seen_notification, name='seen'),
    path('data/', views.notification_data, name='notif-data'),
]