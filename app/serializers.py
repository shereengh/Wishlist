from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item, Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = User
        fields = ["username", "items", "first_name", "last_name"]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['unique_id', 'user']