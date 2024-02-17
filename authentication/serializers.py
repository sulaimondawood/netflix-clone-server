from rest_framework import serializers
from django.conf import settings
from .models import CustomUser
# CustomUser = settings.AUTH_USER_MODEL

class RegisterSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(write_only= True)

  class Meta:
    model= CustomUser
    fields = ['email','username', 'password', 'password2'] 
    extra_kwargs ={'password':{"write_only": True}}

  def validate(self, data):
    if data['password'] != data['password2']:
      raise serializers.ValidationError("Password does not match")
    return data
  
  def create(self, validate_data):
    password = validate_data.get('password')
    user = CustomUser(email = validate_data['email'], username= validate_data['username'])
    user.set_password(password)
    user.save()
    return user


class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)



class UserSerializer(serializers.ModelSerializer):

  class Meta: 
    model= CustomUser
    fields=("id", "username", "first_name")



