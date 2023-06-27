import os
import datetime
import cloudinary

from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from config.settings import ENV

User = get_user_model()
from apps.profiles.models import Profile
from apps.profiles.forms import ProfileForm, UserProfileForm
from apps.notifications.models import Notification
from apps.friends.views import list_relation_receiver_and_sender
from apps.chat.templatetags.chat import add_2_hour


@login_required(login_url='sign_in')
def profile(request, pseudo):
    try:
        profile = Profile.objects.select_related('user').get(pseudo=pseudo)
        if not profile.user.is_email_verified:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    if request.user != profile.user:
        if request.user.is_superuser == False:
            if Notification.objects.filter(type_notif='seen_profile', from_user=request.user, to_user=profile.user).exists():
                last_notif = Notification.objects.filter(type_notif='seen_profile', from_user=request.user, to_user=profile.user).last()
                date_diff = datetime.datetime.now() - add_2_hour(last_notif.date_created.replace(tzinfo=None))
                if date_diff.total_seconds() > 3600:
                    last_notif.delete()
                    
                    Notification.objects.create(type_notif='seen_profile', from_user=request.user, to_user=profile.user)
                    profile.number_views = profile.number_views + 1
                    profile.save()
            else:
                Notification.objects.create(type_notif='seen_profile', from_user=request.user, to_user=profile.user)
                profile.number_views = profile.number_views + 1
                profile.save()
    template = "profiles/profiles.html"
    context = list_relation_receiver_and_sender(request)
    context.update(
        {
            'profile': profile,
        }
    )
    return render(request, template, context=context)


@login_required(login_url='sign_in')
def update_profile(request):
    user = request.user
    user_profile_form = UserProfileForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)
    profile = Profile.objects.get(user=user)
    is_updating_img_profile = False
    is_updating_img_bg = False
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if profile_form.is_valid() and user_profile_form.is_valid():
            if len(request.FILES) != 0:
                for key, value in request.FILES.items():
                    if ENV == 'production':
                        if key == 'img_profile':
                            if profile.is_updating_img_profile:
                                cloudinary.uploader.destroy(str(profile.img_profile))
                            else:
                                is_updating_img_profile = True
                        if key == 'img_bg':
                            if profile.is_updating_img_bg:
                                cloudinary.uploader.destroy(str(profile.img_bg))
                            else:
                                is_updating_img_bg = True
                    else:
                        if key == 'img_profile':
                            if profile.is_updating_img_profile:
                                try:
                                    os.remove(profile.img_profile.path)
                                except:
                                    cloudinary.uploader.destroy(str(profile.img_profile))
                            else:
                                is_updating_img_profile = True
                        if key == 'img_bg':
                            if profile.is_updating_img_bg:
                                try:
                                    os.remove(profile.img_bg.path)
                                except:
                                    cloudinary.uploader.destroy(str(profile.img_bg))
                            else:
                                is_updating_img_bg = True
            user_profile_form.save()
            profile_form.save()
            profile_user = Profile.objects.get(user=user)
            if is_updating_img_profile:
                profile_user.is_updating_img_profile = True
            if is_updating_img_bg:
                profile_user.is_updating_img_bg = True
            profile_user.save()
            return redirect('profiles:profile', pseudo=user.profile.pseudo)
    template = "profiles/update.html"
    context = {
        'user_profile_form' : user_profile_form,
        'profile_form' : profile_form,
    }
    return render(request, template, context=context)