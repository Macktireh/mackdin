from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class Messenger(models.Model):
    
    class Meta:
        ordering = ['date_created',]
        
    sender = models.ForeignKey(User, related_name='sender_msg', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='reciever_msg', on_delete=models.CASCADE)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
