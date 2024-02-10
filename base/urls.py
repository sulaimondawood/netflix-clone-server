from django.urls import path
from .views import PostCreateList

urlpatterns =[
  path('', PostCreateList.as_view(), name='movie-lists')
]