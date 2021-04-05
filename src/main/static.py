'''
Serves static files with the correct MIME type
'''

from django.http.response import HttpResponse
from django.urls import path

from utils import load, static

def serve_static(request, resource):
    del request  # unused
    data, fpath = load.static_file(resource).unwrap()
    content_type = static.mime_type(fpath)
    return HttpResponse(data, content_type=content_type)


app_name = 'static'

urlpatterns = [
    path('<path:resource>', serve_static)
]
