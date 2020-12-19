from django.urls import path

from .views import accounts, register, login

urlpatterns = [
    path('accounts', accounts),
    path('register', register),
    path('login', login),
]
