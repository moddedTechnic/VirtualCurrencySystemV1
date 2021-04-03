'''
Urls for the PWA app
'''

from django.urls import path
from utils import serve
from . import views, settings

app_name = 'pwa'

urlpatterns = [
    path('robots.txt', serve.static_file('robots.txt')),
    path('robots', serve.static_file('robots.txt')),
    path(
        'service-worker.js',
        serve.static_file('scripts/service-worker/worker.js')
    ),
    path(
        'service-worker',
        serve.static_file('scripts/service-worker/worker.js')
    ),
]

if settings.MANIFEST:
    urlpatterns += [
        path('manifest.json', views.manifest()),
        path('manifest', views.manifest()),
    ]
