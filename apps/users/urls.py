from django.urls import path
from django.contrib.auth import views
from apps.users import views as users_views


urlpatterns = [
    path('sign_up/', users_views.sign_up, name='sign_up'),
    path('sign_in/', users_views.sign_in, name='sign_in'),
    path('logout/', users_views.user_logout, name='logout'),
    path('activate-user/<uidb64>/<token>/', users_views.activate_user, name='activate'),
    
    path('reset_password', views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='users/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name='users/password_reset_send.html'), name='password_reset_complete')    
]