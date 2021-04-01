from django.core.handlers.wsgi import WSGIRequest
from django.urls import path

from .views import renders, Title

@renders('users/login.html')
def log_in(request: WSGIRequest) -> Title:
    del request # unused
    return Title('Log In')

app_name = 'users'

urlpatterns = [
    path('login', log_in)
]
