from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
       path('', views.home, name='homePage'),
       path('register/', views.register, name='register'),
       path('login/', views.loginPage, name='loginPage'),
       path('delete/<str:name>/', views.delete, name='delete'),
       path('complete/<str:name>', views.complete, name='complete'),
]