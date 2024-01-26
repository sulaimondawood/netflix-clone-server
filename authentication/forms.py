from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):

  class Meta:
    model= CustomUser
    fields = "__all__"
    # fields = ("username", "email")


class CustomUserCreationForm(UserCreationForm):

  class Meta:
    model= CustomUser
    fields= "__all__"
    # fields = ("username", "email")