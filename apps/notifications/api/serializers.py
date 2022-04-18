from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()
from apps.notifications.models import Notification
from apps.post.models import Post
from apps.comments.models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()
    to_user = UserSerializer()
    # post = PostSerializer()
    # comment_post = CommentSerializer()
    class Meta:
        model = Notification
        fields = '__all__'