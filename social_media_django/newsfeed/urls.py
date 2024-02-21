from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.newsfeed, name='newsfeed'),
    path('p/<str:pk>/', views.post, name='post'),
]