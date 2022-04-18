from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
from apps.profiles.models import Profile
from apps.friends.managers import RelationshipManager




class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    
    class StatusChoices(models.TextChoices):
        send = 'send', _('send')
        accepted = 'accepted', _('accepted')
        
    status = models.CharField(max_length=8, choices=StatusChoices.choices)
    date_sender = models.DateTimeField(blank=True, null=True)
    date_receiver = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    objects = RelationshipManager()
    
    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"