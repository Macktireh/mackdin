
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from rest_framework import routers

from apps.notifications.api.urls import router as router_notifications

router = routers.DefaultRouter()
router.registry.extend(router_notifications.registry)


urlpatterns = [
    path('admin-site/mackind-administration', admin.site.urls, name='admin'),
    path('', include('apps.home.urls')),
    path('accounts/', include('apps.users.urls')),
    path('profile/', include('apps.profiles.urls')),
    path('feed/', include('apps.post.urls')),
    path('comment/', include('apps.comments.urls')),
    path('mynetwork/', include('apps.friends.urls')),
    path('notifications/', include('apps.notifications.urls')),
    
    # urls api
    # path('api/', include('apps.profiles.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        path('api/', include('apps.profiles.api.urls')),
        path('api/', include('apps.notifications.api.urls')),
        # path('api/', include(router.urls)),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
else:
    urlpatterns += [re_path(r'^mediafiles/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),]

# print()
# print()
# for u in urlpatterns: 
#     print(u)
# print()
# print()