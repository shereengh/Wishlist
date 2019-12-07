from django.shortcuts import render

from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import(
	ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, 
	DestroyAPIView, CreateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import authentication, permissions, status


from .models import Item, Profile
from .serializers import (
	ItemSerializer, UserCreateSerializer, MyTokenObtainPairSerializer, 
	ProfileSerializer)

class MyList(ListAPIView):
	permission_classes = [IsAuthenticated, ]
	serializer_class = ItemSerializer
	
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer


class AddItem(APIView):
	serializer_class = ItemSerializer
	permission_classes = [IsAuthenticated]

	def post(self, request):
		request.data['img'] = decode_base64(request.data['img'])
		serializer = ItemSerializer(data=request.data)
		if serializer.is_valid():
			item = Item.objects.create(user = request.user, 
				name = serializer.data['name'], 
				img = request.data['img'], 
				url = serializer.data['url'],
				status = serializer.data['status'], 
			)
			
			item.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteItem(DestroyAPIView):
	queryset = Item.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAuthenticated]


class ItemsList(ListAPIView):
	serializer_class = ProfileSerializer

	def get_queryset(self):
		return Profile.objects.filter(unique_id=self.kwargs['unique_id'])
