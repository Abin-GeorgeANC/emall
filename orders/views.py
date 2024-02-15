
#emall/orders/views.py
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from user.rbac import IsAdmin, IsGetOrAdmin
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    return JsonResponse({"message": "Welcome !"})




class OrderListCreateView(ListCreateAPIView):
    permission_classes = (IsGetOrAdmin,)
    queryset = Orders.objects.filter(is_deleted=False, status=True).order_by('-id')
    serializer_class = OrderSerializer
    pagination_class=LimitOffsetPagination

    # def list(self,*args, **kwargs):
    #     try:
    #         user=self.request.user
    #         if user.user_scope in ("MANAGER","ADMIN"):
    #             queryset=Orders.objects.filter(is_deleted=False, status=True).order_by('-id')
    #         else:
    #             queryset=Orders.objects.filter(is_deleted=False,status=True,customer=user).order_by('-id')
    #         print("queryset:",queryset)
    #         serializer=self.get_serializer(queryset,many=True)
    #         return Response (serializer.data,status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(e)
    #         return Response("Something went wrong",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 
class OrderDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsGetOrAdmin,)
    queryset = Orders.objects.filter(is_deleted=False).order_by('-id')
    serializer_class = OrderSerializer



