'''
The views to render the pages of the main app
'''

from django.core.handlers.wsgi import WSGIRequest

from .utils import renders, Title


@renders('index.html')
def index(request: WSGIRequest) -> Title:
    del request  # unused
    return Title('Hello world')


@renders('about.html')
def about(request: WSGIRequest) -> Title:
    del request  # unused
    return Title('About')

__all__ = [ 'index', 'about' ]
