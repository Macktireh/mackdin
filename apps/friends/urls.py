from django.urls import path
from apps.friends import views

app_name = 'friends'

urlpatterns = [
    path('', views.invites_list_profiles_view, name='my_network'),
    path('connections/', views.my_friends_invites_profiles_view, name='my_friends'),
    path('invitation-received/', views.invites_received_view, name='invitation_received'),
    path('invitation-send/', views.invites_sended_view, name='invitation_send'),
    
    path('invitation/accept/', views.accept_invitation, name='accept_invitation'),
    path('invitation/reject/', views.reject_invitation, name='reject_invitation'),
    path('invitation/cancel/', views.cancel_invitation, name='cancel_invitation'),
    
    path('invitation/send', views.send_invitation, name='send_invitation'),
    path('invitation/remove', views.remove_from_friends, name='remove_invitation'),
]