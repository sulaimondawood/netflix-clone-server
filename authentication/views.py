from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import response, status
from .serializers import RegisterSerializer, LoginSerializer

from django.conf import settings


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)

  return {
    "refresh": str(refresh),
    "access": str(refresh.access_token)
  }


class RegisterUser(APIView):
  
  def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    return response.Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
  

class LoginUser(APIView):

  def post(self, request):
    email = request.data['email']
    password = request.data['password']

    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
      user = authenticate(request, username=email, password=password)
      if user is None:
        return response.Response({'error': "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
      
      get_tokens = get_tokens_for_user(user)
      response_data = {
        "access": get_tokens["access"]
      }
      my_response = response.Response(response_data, status=status.HTTP_200_OK)
      my_response.set_cookie('refresh_token', value=get_tokens["refresh"] ,secure=False,httponly=True, expires=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"])

      return my_response
    
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    
    

