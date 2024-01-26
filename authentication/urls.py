from django.urls import path
from . import views

urlpatterns = [
  path('sign-up/', views.RegisterUser.as_view(), name='sign-up' ),
  path('sign-in/', views.LoginUser.as_view(), name='sign-in')
]