from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<str:order_number>/', views.order_history, name='order_history'),
    path('order_history/<str:order_number>/pdf/<str:pdf_file>', views.download_sheetmusic, name='download_sheetmusic'),
]