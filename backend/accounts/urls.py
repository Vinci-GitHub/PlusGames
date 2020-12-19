from django.urls import path

from .views import accounts, register, login, AuthenticatedUser, logout

urlpatterns = [
    path('accounts', accounts),
    path('register', register),
    path('login', login),
    path('accounts', AuthenticatedUser.as_view()),
    path('logout', logout),
]
