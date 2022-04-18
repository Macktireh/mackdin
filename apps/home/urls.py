from django.urls import path
from apps.home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]