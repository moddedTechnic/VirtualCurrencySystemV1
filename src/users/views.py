'''
Views for the users app.
Provides the functionality for logging in and out
'''

from django.core.handlers.wsgi import WSGIRequest

from main.utils import renders, Title

@renders('users/login.html')
def log_in(request: WSGIRequest) -> Title:
    del request # unused
    return Title('Log In')

@renders('users/login.html')
def log_out(request: WSGIRequest) -> Title:
    del request # unused
    return Title('Log Out')
