from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()
from apps.chat.models import Messenger


@login_required(login_url='sign_in')
def chatroom(request, id):
    other_user = get_object_or_404(User, pk=id)
    current_user = request.user
    qs = Messenger.objects.filter(
        Q(reciever=current_user, sender=other_user) | Q(reciever=other_user, sender=current_user)
    )
    
    template = 'chat/chatroom.html'
    context = {
        'qs': qs,
        'other_user': other_user,
    }
    return render(request, template, context=context)
