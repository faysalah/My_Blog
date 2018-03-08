from django.contrib import admin
from django.urls import path
from .views import index, create, edit, read, add_comment, replay_comment

urlpatterns = [
    path('', index),
    path('create', create),
    path('edit/<int:id>/', edit),
    path('read/<int:id>/', read , name="read"),
    path('comment/<int:id>/', add_comment),
    path('replay/<int:id>/', replay_comment)
]