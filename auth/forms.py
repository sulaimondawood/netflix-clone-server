from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser

class CustomUserChangeForm(UserCreationForm):

  class Meta:
    model= CustomUser
    fields = "__all__"


class CustomUserCreationForm(UserCreationForm):

  class Meta:
    model= CustomUser
    fields= "__all__"