from django.contrib import admin
from django.urls import path
from .views import index, create, edit, read

urlpatterns = [
    path('', index),
    path('create', create),
    path('edit/<int:id>/', edit),
    path('read/<int:id>/', read)
]
