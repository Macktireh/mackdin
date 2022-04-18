from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.notifications.models import Notification
from apps.notifications.api.serializers import NotificationSerializer

@api_view()
def notif_data(request):
    qs = Notification.objects.select_related('from_user').select_related('post').select_related('like_post').select_related('comment_post').all()
    serializer = NotificationSerializer(qs, many=True)
    return Response(serializer.data)


class NotificationViewSet(viewsets.ModelViewSet):
    
    queryset = Notification.objects.select_related('from_user').select_related('post').select_related('like_post').select_related('comment_post').all()
    serializer_class = NotificationSerializer
    