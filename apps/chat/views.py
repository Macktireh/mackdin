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
def chat_view(request):
    qs = Profile.objects.select_related('user').get(user=request.user)
    # last_msg = Messenger.objects.last()

    template = 'chat/chat.html'
    context = {
        'qs': qs,
        'page': 'list_chatroom',
        'start_animation': 'chat',
    }
    return render(request, template, context=context)


@login_required(login_url='sign_in')
def chatroom(request, id):
    try:
        other_user = Profile.objects.select_related('user').get(user=id)
    except:
        return HttpResponseNotFound('<h1>Page not found 404</h1>')
    qs = Profile.objects.select_related('user').get(user=request.user)
    
    if other_user.user not in request.user.profile.friends.all():
        return redirect('post:post_list')
    qs_m = Messenger.objects.messages(request.user, other_user.user)
    qs_m.update(seen=True)

    template = 'chat/chat.html'
    context = {
        'qs_m': qs_m,
        'qs': qs,
        'other_user': other_user,
        'start_animation': 'chat',
    }
    return render(request, template, context=context)


@login_required(login_url='sign_in')
def ajax_load_messages(request, id):
    try:
        other_user = Profile.objects.select_related('user').get(user=id)
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    current_user = request.user
        
    qs = Messenger.objects.filter(seen=False).filter(
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
    qs.update(seen=True)
    
    if request.method == 'POST':
        msg = request.POST.get("msg")
        new_msg = Messenger.objects.create(sender=current_user, reciever=other_user.user, message=msg)
        data.append({
            'msg': new_msg.message,
            'date_created': parserdate(new_msg.date_created.strftime('%d %b %Y %H:%M').lower()),
            'sent': 'right',
        })
        
    return JsonResponse({'data': data})