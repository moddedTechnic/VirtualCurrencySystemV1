from os.path import exists

from django.urls import path
from django.http.response import HttpResponse
from django.conf import settings

def manifest(request):
    for dir in settings.STATICFILES_DIRS:
        fpath = dir / 'manifest.json'
        if exists(fpath):
            with open(fpath, 'r') as f:
                return HttpResponse(f.read(), content_type='text/plain')
    return HttpResponse([ dir / 'manifest.json' for dir in settings.STATICFILES_DIRS])

app_name = 'pwa'

urlpatterns = [
    path('manifest.json', manifest)
]