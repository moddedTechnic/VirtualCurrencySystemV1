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
        serve.static_file('js/service-worker/worker.js')
    ),
    path(
        'service-worker',
        serve.static_file('js/service-worker/worker.js')
    ),
]

if settings.MANIFEST:
    urlpatterns += [
        path('manifest.json', views.manifest()),
        path('manifest', views.manifest()),
        path('apple-touch-icon.png', views.apple_touch_icon()),
        path('apple-touch-icon', views.apple_touch_icon()),
        path('apple-touch-icon-precomposed.png', views.apple_touch_icon()),
        path('apple-touch-icon-precomposed', views.apple_touch_icon()),
    ]
