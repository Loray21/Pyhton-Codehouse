
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('chat/home/', views.home, name='chat-home'),
    path('chat/send/', views.send_chat, name='chat-send')
]
