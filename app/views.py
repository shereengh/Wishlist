from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Item
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User

from .serializers import ItemSerializer, UserCreateSerializer, MyTokenObtainPairSerializer

class ItemList(ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer