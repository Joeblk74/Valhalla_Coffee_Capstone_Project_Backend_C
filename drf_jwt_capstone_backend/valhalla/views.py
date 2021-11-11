from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Coffee
from .serializers import CoffeeSerializer
from .serializers import LoginSerializer
from .serializers import RegisterUserSerializer
from django.contrib.auth import get_user_model
from .models import Login
from .models import RegisterUser

User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_coffee(request):
    coffee = Coffee.objects.all()
    serializer = CoffeeSerializer(coffee, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def login(request):
    login = Login.objects.all()
    serializer = LoginSerializer(login, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register(request):
    register = RegisterUser.objects.all()
    serializer = RegisterUserSerializer(register, many=True)
    return Response(serializer.data)    
