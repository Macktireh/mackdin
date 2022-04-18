from django.urls import path
from apps.profiles import views

app_name = 'profiles'

urlpatterns = [
    # path('<int:id>/<str:firstname>', views.profile, name='profile'),
    path('<str:pseudo>/', views.profile, name='profile'),
    path('update', views.update_profile, name='update_profile'),
]