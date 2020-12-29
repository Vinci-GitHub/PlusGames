from django.urls import path

from .views import (
    register, login, AuthenticatedUser, logout, PermissionAPIView, RoleViewSet,
    AccountGenericAPIView
)

urlpatterns = [
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('account', AuthenticatedUser.as_view()),
    path('permissions', PermissionAPIView.as_view()),
    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('accounts', AccountGenericAPIView.as_view()),
    path('accounts/<str:pk>', AccountGenericAPIView.as_view())
]
