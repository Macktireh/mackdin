from apps.notifications.api import views
from django.urls import path

from rest_framework import routers

router = routers.DefaultRouter()
router.register('notifications', views.NotificationViewSet)

app_name = 'api-notifications'

urlpatterns = [
    path('notifications/', views.notif_data, name='notif-data'),
]