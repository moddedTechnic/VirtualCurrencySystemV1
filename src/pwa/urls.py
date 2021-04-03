from django.urls import path

from .views import serve_static_file

app_name = 'pwa'

urlpatterns = [
    path('manifest.json', serve_static_file('manifest.json')),
    path('manifest', serve_static_file('manifest.json')),
    path('robots.txt', serve_static_file('robots.txt')),
    path('robots', serve_static_file('robots.txt')),
]
