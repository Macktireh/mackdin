from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from apps.notifications.models import Notification


@login_required(login_url='sign_in')
def notification_data(request):
    qs = Notification.objects.all()
    data = []
    for obj in qs:
        if obj.from_user != request.user and obj.to_user == request.user:
            item = {
                "id": obj.id,
                "type_notif": obj.type_notif,
                'from_user': obj.from_user.id,
                'to_user': obj.to_user.id,
                # 'post': obj.post.id,
                'seen': obj.seen,
                'bg_seen': obj.bg_seen,
                "date_created": obj.date_created
            }
            data.append(item)    
    return JsonResponse({'data': data})

@login_required(login_url='sign_in')
def list_notification(request):
    qs = Notification.objects.select_related('from_user').select_related('post').select_related('like_post').select_related('comment_post').all()
    for obj in qs:
        if obj.from_user != request.user and obj.to_user == request.user:
            if obj.seen == False:
                obj.seen = True
                obj.save()
    template = 'post/post_list.html'
    context = {
        'qs': qs,
        'start_animation': 'notif',
        'page': 'notif',
    }
    return render(request, template, context)

@login_required(login_url='sign_in')
def seen_notification(request, id):
    qs = Notification.objects.get(id=id)
    # for obj in qs:
    #     if obj.from_user != request.user and obj.to_user == request.user:
    if qs.bg_seen == False:
        qs.bg_seen = True
        qs.save()
    
    if qs.type_notif == 'Like_Post' or qs.type_notif == 'Add_Post' or qs.type_notif == 'Add_Comment':
        return redirect('post:post_detail', qs.post.id)
    elif qs.type_notif == 'invitation_accepted':
        return redirect('friends:my_friends')
    elif qs.type_notif == 'invitation_send':
        return redirect('friends:invitation_received')
    return redirect('notifications:notif')
        