from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('word_analyzer.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r'^static/(?P<path>.*)$',
            serve,
            {'document_root': settings.MKDOCS_STATIC_PATH},
        ),
    ]
