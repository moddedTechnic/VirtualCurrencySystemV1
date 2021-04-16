'''
Views for the users app.
Provides the functionality for logging in and out
'''

from collections import namedtuple
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from main.utils import Context, Renders, Title, View


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
                return redirect('users:account')
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


@Renders('users/account.html')
def account(request: WSGIRequest) -> HttpResponse:
    del request  # unused
    Transaction = namedtuple(
        'Transaction', ('id', 'other_name', 'to_me', 'amount', 'date'))
    transactions = [
        Transaction(0, 'Fred', False, 100, datetime(2021, 4, 10, 12, 30)),
        Transaction(1, 'Bank', True, 250, datetime(2021, 1, 1, 0, 0)),
    ]
    balance = sum(map(
        lambda t: t.amount * (2 * int(t.to_me) - 1),
        transactions
    ))
    recent_transactions = sorted(transactions, key=lambda t: t.date, reverse=True)
    return Context(title='Account', balance=balance, recent_transactions=recent_transactions)
