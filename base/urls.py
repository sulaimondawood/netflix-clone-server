from django.urls import path
from .views import PostCreateList, TagList, CategoryCreateList

urlpatterns =[
  path('', PostCreateList.as_view(), name='movie-list'),
  path('tags/', TagList.as_view(), name='tag-list' ),
  path('category/', CategoryCreateList.as_view(), name='tag-list' ),
]