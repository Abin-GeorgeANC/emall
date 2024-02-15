#emall/orders/urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('',  index, name="index"),
    path("orderlist/", OrderListCreateView.as_view(), name="orderlist"),
    path("orderdetails/<int:pk>", OrderDetailsAPIView.as_view(), name="orderdetails")
]