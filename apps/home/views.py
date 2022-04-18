from apps.profiles.models import Profile
from django.shortcuts import redirect, render


def home(request):
    user = request.user
    template = "home/index.html"
    context = {
        'start_animation': 'home',
    }
    if user.is_authenticated:
        return redirect('post:post_list')
    
    return render(request, template, context=context)