from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser


class CustomUserManager(BaseUserManager):

  def create_user(self,email,password, **extra_fields):
    if not email:
      raise ValueError("Email field cannot be empty")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get("is_staff") is not True:
      raise ValueError("Superuser must have is_staff equals true")
    
    if extra_fields.get('is_superuser') is not True:
      raise ValueError("Superuser must have is_superuser set to true")
    
    if extra_fields.get('is_active') is not True:
      raise ValueError("Super user must have is active equals true")
    return self.create_user(email,password,**extra_fields)
    


class CustomUser(AbstractUser):
  email = models.EmailField(unique=True)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS= ()

  objects = CustomUserManager()

  def __str__(self):
    return self.username

