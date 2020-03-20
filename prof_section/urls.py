from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginView),
    path('index/', views.index),
    path('getqr/', views.getqr),
    path('scan/', views.scan),
    path('test/', views.test),
]