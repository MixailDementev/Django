from django.urls import path
from .views import AllOrderViews, DetailOrder

urlpatterns = [
    path('orders/<int:id_customer>', AllOrderViews.as_view(), name='orders'),
    path('orders_customer/<int:pk>', DetailOrder.as_view(), name='detail_orders'),
]