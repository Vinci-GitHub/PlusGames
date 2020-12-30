from django.urls import path
from products.views import ProductGenericAPIView

urlpatterns = [
    path('products', ProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view())
]
