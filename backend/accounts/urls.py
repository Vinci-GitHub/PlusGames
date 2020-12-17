from django.urls import path

from .views import accounts, register

urlpatterns = [
    path('accounts', accounts),
    path('register', register)
]
