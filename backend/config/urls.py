# from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include

# from apiv1 import views
# from apiv1.urls import router as apiv1_router
# from rest_framework import routers

# api_router = routers.DefaultRouter()
# api_router.registry.extend(apiv1_router.registry)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),

    # path('api/', include('trade.apitrade.urls')),
    # url(r'^v2/', include(api_router.urls)),
    # path('', include('trade.urls')),
    # path('', views.TestView, name='test'),
]
