import random
from apps.profiles.models import Profile
from django.shortcuts import redirect, render


def home(request):
    user = request.user
    template = "home/index.html"
    # template = "index.html"
    # mens = [f"https://randomuser.me/api/portraits/men/{i}.jpg" for i in range(0, 80)] + [f"https://xsgames.co/randomusers/assets/avatars/male/{i}.jpg" for i in range(0, 78)]
    # womens = [f"https://randomuser.me/api/portraits/women/{i}.jpg" for i in range(0, 80)] + [f"https://xsgames.co/randomusers/assets/avatars/female/{i}.jpg" for i in range(0, 78)]
    # images = mens + womens
    # random.shuffle(images)

    context = {
        'start_animation': 'home',
        # "images": images,
        # "l": len(images),
    }

    # return render(request, template, context=context)

    if user.is_authenticated:
        return redirect('post:post_list')
    
    return render(request, template, context=context)