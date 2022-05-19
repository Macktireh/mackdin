import json
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.humanize.templatetags.humanize import naturaltime

from apps.comments.models import Comment, ReponseComment, LikeComment
from apps.comments.forms import CommentForm, ReponseCommentForm
from apps.post.models import Post
from apps.chat.templatetags.chat import timestr

User = get_user_model()


def comment_view(request):
    qs_comment = Comment.objects.select_related('author').all()
    form_comment = CommentForm(request.POST)
    form_reponse = ReponseCommentForm(request.POST)
    
    context = {
        'qs_comment': qs_comment,
        'form_comment': form_comment,
        'form_reponse': form_reponse
    }
    return context


@login_required(login_url='sign_in')
def comment_all_data(request):  
    qs_comment = Comment.objects.select_related("author").select_related("post").all()
    qs_user = User.objects.prefetch_related("profile")
    
    data = []
    
    for obj in qs_comment:
        item = {
            'id': obj.id,
            'comment_author': obj.author.email,
            'comment_author_id': obj.author.id,
            'comment_author_first_name': obj.author.first_name,
            'comment_author_last_name': obj.author.last_name,
            'comment_message': obj.message,
            'comment_date_added': naturaltime(obj.date_added),
            'post_id': obj.post.id,
            'post_author': obj.post.author.email,
            'post_message': obj.post.message,
            'post_img': obj.post.img.url,
            'user_pseudo': qs_user.get(id=obj.author.id).profile.pseudo,
            'user_bio': qs_user.get(id=obj.author.id).profile.bio,
            'user_img_profile': qs_user.get(id=obj.author.id).profile.img_profile.url,
            'current_user': request.user.email,
        }
        data.append(item)
  
    return JsonResponse({'data': data})

@login_required(login_url='sign_in')
def get_comments_post(request, post_id):  
    qs_comment = Comment.objects.select_related("author").select_related("post").all()
    qs_user = User.objects.prefetch_related("profile")
    
    data = []
    
    for obj in qs_comment:
        if post_id == str(obj.post.id):
            item = {
                'id': obj.id,
                'comment_author': obj.author.email,
                'comment_author_id': obj.author.id,
                'comment_author_first_name': obj.author.first_name,
                'comment_author_last_name': obj.author.last_name,
                'comment_message': obj.message,
                'comment_date_added': timestr(naturaltime(obj.date_added)),
                'post_id': obj.post.id,
                'post_author': obj.post.author.email,
                'post_message': obj.post.message,
                'post_img': obj.post.img.url if obj.post.img else None,
                'user_pseudo': qs_user.get(id=obj.author.id).profile.pseudo,
                'user_bio': qs_user.get(id=obj.author.id).profile.bio,
                'user_img_profile': qs_user.get(id=obj.author.id).profile.img_profile.url,
                'current_user': request.user.email,
            }
            data.append(item)
        
        
  
    return JsonResponse({'data': data})


@login_required(login_url='sign_in')
def add_update_comment_view(request):
    user = request.user
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # print('\n\najax request with fetch')
        
        don = json.load(request)
        
        message = don['message'] 
        id_post = don['id_post'] 
        id_comment = don['id_comment'] 
        
        if id_comment:
            if Comment.objects.filter(id=id_comment).exists():
                comment_post = Comment.objects.get(id=id_comment)
                comment_post.message = message
                comment_post.save()
        else:
            comment_post = Comment.objects.create(author=user, post_id=id_post, message=message)
        
        data = {
            'id': comment_post.id,
            'comment_author': comment_post.author.email,
            'comment_author_first_name': comment_post.author.first_name,
            'comment_author_last_name': comment_post.author.last_name,
            'comment_message': comment_post.message,
            'comment_date_added': naturaltime(comment_post.date_added),
            
            'post_author': comment_post.post.author.email,
            'post_id': comment_post.post.id,
            
            'user_profile_pseudo': comment_post.author.profile.pseudo,
            'user_profile_bio': comment_post.author.profile.bio,
            'user_profile_img': comment_post.author.profile.img_profile.url if comment_post.author.profile.img_profile else "",
            
            'current_user': request.user.email
        }
        
        return JsonResponse(data, status=200)


@login_required(login_url='sign_in')
def delete_comment(request):
    id_comment = request.POST.get("id_comment")
    obj = Comment.objects.get(id=id_comment)
    obj.delete()
    return JsonResponse({'action': "commentaire supprimer"})



