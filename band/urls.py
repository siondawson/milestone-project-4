from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='band'),
    path('about/', views.about, name='about'),
    path('add/', views.add_concert, name='add_concert'),
    path('edit/<int:concert_id>/', views.edit_concert, name='edit_concert'),
    path('delete/<int:concert_id>/', views.delete_concert, name='delete_concert'),
    
]
