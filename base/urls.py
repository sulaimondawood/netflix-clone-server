from django.urls import path
from .views import PostCreateList, TagList, CategoryCreateList, PostDeleteEditRetrieve

urlpatterns =[
  path('', PostCreateList.as_view(), name='movie-list'),
  path('<str:pk>/', PostDeleteEditRetrieve.as_view(), name="single-movie" ),
  path('tags/', TagList.as_view(), name='tag-list' ),
  path('category/', CategoryCreateList.as_view(), name='tag-list' ),
]