from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_sheetmusic, name='sheetmusic'),
    path('<int:sheetmusic_id>/', views.sheetmusic_detail, name='sheetmusic_detail'),
    path('add', views.add_sheetmusic, name='add_sheetmusic'),
    path('edit/<int:sheetmusic_id>/', views.edit_sheetmusic, name='edit_sheetmusic'),

]
