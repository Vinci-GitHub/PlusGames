from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from apiv1 import views
from apiv1.urls import router as apiv1_router
from rest_framework import routers

api_router = routers.DefaultRouter()
api_router.registry.extend(apiv1_router.registry)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.TestView, name='test'),
    url(r'^v2/', include(api_router.urls)),
]
