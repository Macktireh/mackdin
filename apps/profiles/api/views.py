from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.comments.models import Comment
from apps.post.models import Post

from apps.profiles.api.serializers import ProfileSerializer
from apps.profiles.models import Profile


@api_view()
def get_list_profiles(request):
    qs = Profile.objects.select_related('user').all()
    serializers = ProfileSerializer(qs, many=True)
    # print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    return Response(serializers.data)


@api_view()
def get_profile(request, id):
    qs = get_object_or_404(Profile, pk=id)
    serializer = ProfileSerializer(qs)
    # print(serializer.data)
    return Response(serializer.data)