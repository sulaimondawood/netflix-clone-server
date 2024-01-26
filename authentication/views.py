from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import response, status
from .serializers import RegisterSerializer


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
      return response.Response(serializer.data ,status=status.HTTP_201_CREATED)
    return response.Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)