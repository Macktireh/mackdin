from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()
from apps.chat.models import Messenger
from apps.profiles.models import Profile


def parserdate(date):
    date = date.replace('jan', 'janv')
    date = date.replace('feb', 'févr')
    date = date.replace('mar', 'mars')
    date = date.replace('apr', 'avr')
    date = date.replace('may', 'mai')
    date = date.replace('jun', 'juin')
    date = date.replace('jul', 'juill')
    date = date.replace('aug', 'août')
    date = date.replace('sep', 'sept')
    date = date.replace('oct', 'oct')
    date = date.replace('nov', 'nov')
    date = date.replace('dec', 'déc')
    return date

@login_required(login_url='sign_in')
def chat_api_view(request):
    qs = Profile.objects.select_related('user').get(user=request.user)
    data = []
    for obj in qs.friends.all():
        last_msgs = Messenger.objects.filter(reciever=request.user, sender=obj)
        data += [{
            'id': msg.id,
            'message': msg.message,
            'seen': msg.seen,
            'sender': msg.sender.first_name,
            'reciever': msg.reciever.first_name,
        } for msg in last_msgs]
    
    return JsonResponse({'data': data})



@login_required(login_url='sign_in')
def chat_view(request):
    qs = Profile.objects.select_related('user').get(user=request.user)
    
    last_msgs = []
    for obj in qs.friends.all():
        last_msg = Messenger.objects.filter(
            Q(reciever=request.user, sender=obj) | Q(reciever=obj, sender=request.user)
        ).last()
        if last_msg:
            last_msgs.append({
                'sender_id': last_msg.sender.id,
                'reciever_id': last_msg.reciever.id,
                'msg': last_msg.message,
                'seen': 'oui' if last_msg.seen else 'non',
                'date_created': last_msg.date_created
            })

    template = 'chat/chat.html'
    context = {
        'qs': qs,
        'page': 'list_chatroom',
        'start_animation': 'chat',
        'last_msgs': last_msgs,
    }
    return render(request, template, context=context)


@login_required(login_url='sign_in')
def chatroom(request, uid):
    try:
        other_user = Profile.objects.select_related('user').get(uid=uid)
    except:
        return HttpResponseNotFound('<h1>Page not found 404</h1>')
    qs = Profile.objects.select_related('user').get(user=request.user)
    last_msgs = []
    for obj in qs.friends.all():
        last_msg = Messenger.objects.filter(
            Q(reciever=request.user, sender=obj) | Q(reciever=obj, sender=request.user)
        ).last()
        if last_msg:
            last_msgs.append({
                'sender_id': last_msg.sender.id,
                'reciever_id': last_msg.reciever.id,
                'msg': last_msg.message,
                'seen': 'oui' if last_msg.seen else 'non',
                'date_created': last_msg.date_created
            })
    
    if other_user.user not in request.user.profile.friends.all():
        return redirect('chats:chat')
    qs_my_msg = Messenger.objects.filter(
                Q(reciever=request.user, sender=other_user.user)
            )
    qs_my_msg.update(seen=True)
    qs_my_msg.update(sent=True)
    
    qs_m = Messenger.objects.messages(request.user, other_user.user)

    template = 'chat/chat.html'
    context = {
        'qs_m': qs_m,
        'qs': qs,
        'other_user': other_user,
        'last_msgs': last_msgs,
        'start_animation': 'chat',
    }
    return render(request, template, context=context)


@login_required(login_url='sign_in')
def ajax_load_messages(request, uid):
    try:
        other_user = Profile.objects.select_related('user').get(uid=uid)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    current_user = request.user
        
    qs = Messenger.objects.filter(sent=False).filter(
                Q(reciever=current_user, sender=other_user.user)
            )
    
    data = []
    for obj in qs:
        item = {
            'msg': obj.message,
            'date_created': parserdate(obj.date_created.strftime('%d %b %Y %H:%M').lower()),
            'sent': 'right' if obj.sender == current_user else 'left',
        }
        data.append(item)
    qs.update(sent=True)
    
    if request.method == 'POST':
        Messenger.objects.filter(seen=False).filter(
                Q(reciever=current_user, sender=other_user.user)
            ).update(seen=True)
        # qs.update(sent=True)
        msg = request.POST.get("msg")
        new_msg = Messenger.objects.create(sender=current_user, reciever=other_user.user, message=msg)
        data.append({
            'msg': new_msg.message,
            'date_created': parserdate(new_msg.date_created.strftime('%d %b %Y %H:%M').lower()),
            'sent': 'right',
        })
        
    return JsonResponse({'data': data})