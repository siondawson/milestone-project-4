from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='band'),
    path('about/', views.about, name='about'),
    path('add/', views.add_concert, name='add_concert'),
    
]
