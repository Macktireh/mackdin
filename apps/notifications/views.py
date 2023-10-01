import asyncio
from collections.abc import AsyncGenerator

from asgiref.sync import async_to_sync, sync_to_async

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    JsonResponse,
    StreamingHttpResponse,
)
from django.shortcuts import get_object_or_404, redirect, render

from apps.notifications.models import Notification


def qs_notification_data():
    return Notification.objects.all()


# @sync_to_async
@login_required(login_url="sign_in")
# @async_to_sync
def notification_data(request) -> JsonResponse:
    qs = Notification.objects.all().filter(to_user=request.user)

    data = []
    for obj in qs:
        if obj.from_user != request.user and obj.to_user == request.user:
            item = {
                "id": obj.id,
                "type_notif": obj.type_notif,
                "from_user": obj.from_user.id,
                "to_user": obj.to_user.id,
                # 'post': obj.post.id,
                "seen": obj.seen,
                "bg_seen": obj.bg_seen,
                "date_created": obj.date_created,
            }
            data.append(item)
    return JsonResponse({"data": data})


@login_required(login_url="sign_in")
def list_notification(request) -> HttpResponse:
    qs = (
        Notification.objects.select_related("from_user")
        .select_related("post")
        .select_related("like_post")
        .select_related("comment_post")
        .all()
        .filter(to_user=request.user)
    )
    
    is_notif = False
    for obj in qs:
        if obj.from_user != request.user and obj.to_user == request.user:
            is_notif = True
            if obj.seen == False:
                obj.seen = True
                obj.save()

    paginator = Paginator(qs, 10)
    page = request.GET.get("page")
    num = paginator.num_pages

    if page is None: page = 1
    if int(page) > num: return HttpResponseNotFound("<h1>Page not found 404</h1>")
    qs = paginator.get_page(page)
    template = "post/post_list.html"
    context = {
        "qs": qs,
        "is_notif": is_notif,
        "page": "notif",
        "start_animation": "notif",
    }

    if request.is_ajax():
        return render(request, "notifications/card-notification.html", context)
    
    return render(request, template, context)


@login_required(login_url="sign_in")
def seen_notification(
    request, id
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    qs = Notification.objects.get(id=id)
    # for obj in qs:
    #     if obj.from_user != request.user and obj.to_user == request.user:
    if qs.bg_seen == False:
        qs.bg_seen = True
        qs.save()

    if (
        qs.type_notif == "Like_Post"
        or qs.type_notif == "Add_Post"
        or qs.type_notif == "Add_Comment"
    ):
        return redirect("post:post_detail", qs.post.uid)
    elif qs.type_notif == "invitation_accepted":
        return redirect("friends:my_friends")
    elif qs.type_notif == "invitation_send":
        return redirect("friends:invitation_received")
    return redirect("notifications:notif")


async def stream_notifications() -> AsyncGenerator[str, None]:
    latest_notif = None

    while True:
        current_notif = await Notification.objects.order_by("-id").afirst()

        # If we have a new message yield that
        if latest_notif != current_notif:
            yield "data: {current_notif.text}\n\n"
            latest_notif = current_notif

        await asyncio.sleep(3)

async def stream_notifications_view(request: HttpRequest) -> StreamingHttpResponse:
    return StreamingHttpResponse(
        streaming_content=stream_notifications(),
        content_type="text/event-stream",
    )
