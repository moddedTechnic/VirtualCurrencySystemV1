'''
VirtualCurrency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
'''

from django.contrib import admin
from django.urls import path, include

from main.utils import Title, View

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', include('users.urls')),
    path('static', include('main.static')),
    path('', View('index.html', Title('VCS')), name='home'),
    path('about', View('about.html', Title('About')), name='about'),
]
