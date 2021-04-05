'''
VirtualCurrency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
'''

from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', include('users.urls')),
    path('static', include('main.static')),
    path('', views.index),
    path('about', views.about),
]
