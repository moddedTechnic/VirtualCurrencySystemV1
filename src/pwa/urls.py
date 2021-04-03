'''
Urls for the PWA app
'''

from django.urls import path
from utils import serve

app_name = 'pwa'

urlpatterns = [
    path('manifest.json', serve.static_file('manifest.json')),
    path('manifest', serve.static_file('manifest.json')),
    path('robots.txt', serve.static_file('robots.txt')),
    path('robots', serve.static_file('robots.txt')),
]
