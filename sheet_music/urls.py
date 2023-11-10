from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_sheetmusic, name='sheetmusic'),
    path('<sheetmusic_id>', views.sheetmusic_detail, name='sheetmusic_detail'),

]
