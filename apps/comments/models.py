from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from apps.post.models import Post

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    message = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(User, related_name='users_comment_like', blank=True, default=None)
    
    def __str__(self):
        return f"Comment-{self.id}-{self.author.first_name}"

class ReponseComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reponse_comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reponse_comment')
    message = models.CharField(blank=True, null=True, max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author.first_name} {self.author.last_name}"

class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like_comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='like_comment')
    LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    )
    value = models.CharField(choices=LIKE_CHOICES, max_length=10)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}   -   Comment Id: {self.post.id}"