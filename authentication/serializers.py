from rest_framework import serializers
from django.conf import settings

CustomUser = settings.AUTH_USER_MODEL

class RegisterSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(write_only= True)

  class Meta:
    model= CustomUser
    fields = ['email','username', 'password' 'password2'] 
    extra_kwargs ={'password':{"write_only": True}}

  def validate(self, data):
    if data['password'] != data['password2']:
      raise serializers.ValidationError("Password does not match")
    return data
  
  # def create(self, validate_data):
  #   passoword = validate_data.get('password')
  #   user = CustomUser(**validate_data)
  #   user.set_password(passoword)
  #   user.save()