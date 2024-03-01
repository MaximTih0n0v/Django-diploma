from django.contrib import admin
from django.urls import include, path
from djangoDiploma import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls', namespace='main')),
    path('catalog/', include('apps.products.urls', namespace='catalog')),
    path('user/', include('apps.users.urls', namespace='user')),
    path('reservation/', include('apps.reservation.urls', namespace='reservation')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
