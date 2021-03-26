from django.http.response import HttpResponse
from django.urls import path

from .views import renders, Title

@renders('users/login.html')
def log_in(request):
    return Title('Log In')

app_name = 'users'

urlpatterns = [
    path('login', log_in)
]
