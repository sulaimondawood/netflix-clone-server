from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
  form = CustomUserChangeForm
  add_form = CustomUserCreationForm

admin.site.register(CustomUser, CustomUserAdmin)