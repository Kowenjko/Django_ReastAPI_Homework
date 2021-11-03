from django.shortcuts import render
from django.http import Http404
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import serializers, viewsets
from .models import Address, UserList
from .serializer import UserListSerializer,AddressListSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset=UserList.objects.all().order_by('id')
    serializer_class = UserListSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset=Address.objects.all().order_by('id')
    serializer_class = AddressListSerializer

class AddressView:
    class AddressList(APIView):
        def get(self,request,format=None):
            address = Address.objects.all()
            serializer = AddressListSerializer(address,many = True)
            return Response(serializer.data)

        def post(self,request,format=None):
            serializer = AddressListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

