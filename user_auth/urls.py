from django.urls import path
from .views import index, register, logout_view

urlpatterns = [
    path('', index, name="index"),
    path('register', register, name="register"),
    path('logout', logout_view, name="logout")
]
