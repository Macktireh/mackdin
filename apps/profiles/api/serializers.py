from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.comments.models import Comment
from apps.post.models import Post

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',)

# class ProfileSerializer(serializers.ModelSerializer):
#     author = UserSerializer()
#     img = serializers.ImageField()
#     liked = UserSerializer(read_only=True, many=True)
#     class Meta:
#         model = Post
#         fields = ('id', 'author', 'message', 'img', 'liked', 'date_created',)
    
class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    pseudo = serializers.CharField(max_length=48)
    bio = serializers.CharField(max_length=250)
    img_profile = serializers.ImageField()
    phone = serializers.CharField(max_length=20)
    adress = serializers.CharField(max_length=128)
    town = serializers.CharField(max_length=68)
    region = serializers.CharField(max_length=68)
    country = serializers.CharField(max_length=45)
    description = serializers.CharField()
    number_views = serializers.IntegerField(default=0)
    date_updated = serializers.DateTimeField()
    link_linkedin = serializers.URLField()
    link_gitthub = serializers.URLField()
    link_twitter = serializers.URLField()
    link_mysite = serializers.URLField()
    
    