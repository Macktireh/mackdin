from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()

class MessengerManager(models.Manager):
    
    def messages(self, current_user, other_user):
        """
        Args:
            current_user : utilisateur actuelle ou connecté
            other_user : utilisateur qui chate avec l'utilisateur connecté
        Returns:
            cette méthode renvoie tout les messages entre ces deux utilisateurs
        """
        qs = Messenger.objects.filter(
                Q(reciever=current_user, sender=other_user) | Q(reciever=other_user, sender=current_user)
            )
        return qs

class Messenger(models.Model):
    class Meta:
        ordering = ['date_created',]
        
    sender = models.ForeignKey(User, related_name='sender_msg', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='reciever_msg', on_delete=models.CASCADE)
    message = models.TextField()
    seen = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    objects = MessengerManager()
    
    def __str__(self):
        return f"CHAT sender: {self.sender.first_name} | reciever: {self.reciever.first_name}"
    
    def get_messages(self):
        return f"{self.message}"
