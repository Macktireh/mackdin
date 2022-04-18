from django.urls import path

from apps.profiles.api import views

app_name = 'api-profiles'

urlpatterns = [
    path('profiles/', views.get_list_profiles),
    path('profiles/<int:id>/', views.get_profile),
]