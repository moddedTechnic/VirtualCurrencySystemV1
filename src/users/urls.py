'''
Urls for users

- /login
- /logout
'''

from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.log_in),
    path('logout', views.log_out),
]
