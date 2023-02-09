from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('', include('apps.fructs.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('apps.users.urls')),
    # path('social-auth/',include('social_django.urls', namespace='social')),
    path('images/', include('apps.images.urls', namespace='images')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)