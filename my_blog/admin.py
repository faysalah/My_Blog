from django.contrib import admin
from .models import Category, Article, Comment, CommentReplay, Favourite, Bookmark
# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(CommentReplay)
admin.site.register(Favourite)
admin.site.register(Bookmark)
