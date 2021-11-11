from typing import FrozenSet
from rest_framework import serializers
from .models import Coffee
from .models import Login
from .models import RegisterUser


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['FirstName','LastName', 'UserName', 'Password', 'Email', 'PhoneNumber']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['user_id', 'password']

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ['flavor', 'origin', 'description', 'price', 'user_id']
