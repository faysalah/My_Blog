from django.contrib import admin
from django.urls import path
from .views import index, create, edit, read, published, drafts, add_comment, replay_comment, do_favourite, category_filter, do_bookmark, bookmarked

urlpatterns = [
    path('', index),
    path('create', create),
    path('edit/<int:id>/', edit),
    path('read/<int:id>/', read , name="read"),
    path('comment/<int:id>/', add_comment),
    path('replay/<int:id>/', replay_comment),
    path('favourite/<int:id>/', do_favourite),
    path('published', published),
    path('drafts', drafts),
    path('category/<int:id>/', category_filter),
    path('bookmark/<int:id>/', do_bookmark),
    path('bookmarked', bookmarked)
]