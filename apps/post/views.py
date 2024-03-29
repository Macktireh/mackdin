import os
import cloudinary

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from apps.notifications.models import Notification
from apps.profiles.models import Profile
from apps.comments.views import comment_view
from apps.post.models import LikePost, Post
from apps.post.forms import PostForm


@login_required(login_url="sign_in")
def post_create_list_view(
    request, *args, **kwargs
) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    page = request.GET.get("page")
    if page is None:
        page = 1
    posts = cache.get(f"posts_list_{page}")

    if posts is None:
        _posts = (
            Post.objects.select_related("author").prefetch_related("post_comment").all()
        )
        current_user = Profile.objects.select_related("user").get(user=request.user)

        paginator = Paginator(_posts, 6)
        num = paginator.num_pages

        if int(page) > num:
            return HttpResponseNotFound("<h1>Page not found 404</h1>")

        posts = paginator.get_page(page)
        try:
            cache.set(f"posts_list_{page}", posts, 60 * 60 * 24)
        except Exception:
            pass

    AddPostForm = PostForm()

    if "submit_p_form" in request.POST:
        AddPostForm = PostForm(request.POST, request.FILES)
        if AddPostForm.is_valid():
            instance = AddPostForm.save(commit=False)
            instance.author = request.user
            instance.save()
            AddPostForm = PostForm()

            # notifier pour le nouveau post aux amis
            if request.user.friends:
                for to_user in request.user.friends.all():
                    Notification.objects.create(
                        type_notif="Add_Post",
                        from_user=request.user,
                        to_user=to_user.user,
                        post=instance,
                    )

            return redirect("post:post_list")

    context = {
        "start_animation": "feed",
        "posts": posts,
        "AddPostForm": AddPostForm,
        "page": "list",
        "domain": get_current_site(request),
        "is_ajax": request.is_ajax(),
        "page_number": page,
    }
    context.update(comment_view(request))

    if request.is_ajax():
        return render(request, "post/components/post-detail.html", context)

    return render(request, "post/post_list.html", context)


@cache_page(60 * 15)
@login_required(login_url="sign_in")
def post_detail_view(request, uid):
    try:
        post = (
            Post.objects.select_related("author")
            .prefetch_related("post_comment")
            .get(uid=uid)
        )
    except:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    template = "post/post_list.html"
    context = {
        "start_animation": "feed",
        "posts": [post],
        "page": "detail",
    }
    context.update(comment_view(request))
    return render(request, template, context)


@login_required(login_url="sign_in")
def update_post(request, uid):
    post_edit = get_object_or_404(Post, uid=uid)
    if post_edit.author != request.user:
        return HttpResponseNotFound("<h1>Page Not Found 404</h1>")
    posts = Post.objects.all()
    if request.method == "POST":
        if len(request.FILES) != 0:
            if post_edit.img:
                if len(post_edit.img) > 0:
                    if settings.ENV == "production":
                        cloudinary.uploader.destroy(str(post_edit.img))
                    else:
                        try:
                            os.remove(post_edit.img.path)
                        except:
                            cloudinary.uploader.destroy(str(post_edit.img))
            post_edit.img = request.FILES["img"]
        post_edit.message = request.POST.get("message")
        post_edit.save()
        return redirect("post:post_list")

    template = "post/post_list.html"
    context = {
        "start_animation": "feed",
        "posts": posts,
        "post_edit": post_edit,
        "page": "update",
    }
    return render(request, template, context)


# def add_post(request):
#     user = request.user
#     AddPostForm = PostForm(request.POST or None, request.FILES or None)
#     if request.is_ajax():
#         if AddPostForm.is_valid():
#             instance = AddPostForm.save(commit=False)
#             instance.author = user
#             instance.save()
#             post = Post.objects.values()
#             return JsonResponse({'status': 'success', 'post_data': list(post)})
#         else:
#             return JsonResponse({'status': 'error'})


@login_required(login_url="sign_in")
def delete_post(request, uid):
    user = request.user
    # if request.method == 'POST':
    #     p_id = request.POST.get('post_id')
    #     instance = Post.objects.get(pk=p_id)
    #     if user == instance.author:
    #         instance.delete()
    #         return JsonResponse({'status': 'Post supprimer'})
    # else:
    #     return JsonResponse({'status': 'error'})
    instance = get_object_or_404(Post, uid=uid)
    if user == instance.author:
        instance.delete()
    return redirect("post:post_list")


@login_required(login_url="sign_in")
def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = LikePost.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value == "Like":
                like.value = "Unlike"
            else:
                like.value = "Like"
        else:
            like.value = "Like"

        post_obj.save()
        like.save()

        data = {
            "value": str(like.value),
        }
        return JsonResponse(data, safe=False)
    return redirect("post:post_list")
