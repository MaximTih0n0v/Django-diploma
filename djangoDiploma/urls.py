from django.contrib import admin
from django.urls import include, path
from djangoDiploma.settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls', namespace='main')),
    path('catalog/', include('apps.products.urls', namespace='catalog'))

]

if DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]