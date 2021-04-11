'''
Serves static files with the correct MIME type
'''

from django.http.response import HttpResponse
from django.urls import path

from utils import load


def serve_static(request, resource):
    del request  # unused
    data, _, content_type = load.static_file(resource).unwrap()
    return HttpResponse(data, content_type=content_type)


app_name = 'static'

urlpatterns = [
    path('<path:resource>', serve_static),
]
