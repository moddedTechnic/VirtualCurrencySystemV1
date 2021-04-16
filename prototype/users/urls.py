'''
Urls for users

- /login
- /logout
'''

from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('account', views.account, name='account'),
]
