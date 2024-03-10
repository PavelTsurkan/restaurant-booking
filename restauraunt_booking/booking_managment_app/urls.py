from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('add_booking/', views.add_booking, name='add_book'),
]