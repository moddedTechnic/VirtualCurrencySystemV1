'''
Views for the users app.
Provides the functionality for logging in and out
'''

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from main.utils import Context, Title, View


def log_in(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form  = AuthenticationForm()
    return View(
        'users/login.html', Title('Log In'), Context(form=form))(request)


def log_out(request: WSGIRequest) -> HttpResponse:
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('/')
