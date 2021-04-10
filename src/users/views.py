'''
Views for the users app.
Provides the functionality for logging in and out
'''

from django.core.handlers.wsgi import WSGIRequest

from main.utils import Renders, Title

@Renders('users/login.html')
def log_in(request: WSGIRequest) -> Title:
    del request # unused
    return Title('Log In')

@Renders('users/login.html')
def log_out(request: WSGIRequest) -> Title:
    del request # unused
    return Title('Log Out')
