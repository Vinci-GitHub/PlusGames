from django.urls import path

from .views import register, login, AuthenticatedUser, logout, \
    PermissionAPIView, RoleViewSet

urlpatterns = [
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('accounts', AuthenticatedUser.as_view()),
    path('permissions', PermissionAPIView.as_view()),
    path('role', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]










