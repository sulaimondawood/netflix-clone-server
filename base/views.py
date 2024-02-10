from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post, Tag, Category
from .serializers import PostSerializer, PostCreateSerializer,TagListSerializer, CategoryListSerializer

 
class TagList(APIView):
  qs = Tag.objects.all()

  def get(self, request):
    serializer = TagListSerializer(self.qs, many=True)
    return Response({'message':"successfull",
                     "status":True,
                     "data": serializer.data}, status=status.HTTP_200_OK)


class CategoryCreateList(APIView):
  qs = Category.objects.all()

  def get(self, request):
    serializer = CategoryListSerializer(self.qs, many=True)
    return Response({'message':"successfull",
                     "status":True,
                     "data": serializer.data}, status=status.HTTP_200_OK)

class PostCreateList(APIView):
  
  def get(self, request):
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True)

    return Response({
      "data":serializer.data,
      "message": "successfull",
      "status": True
    }, status=status.HTTP_200_OK)

  
  def post(self, request):
    serializer = PostCreateSerializer(data= request.data,)
    if serializer.is_valid(raise_exception=True):
      serializer.save(author = request.user)
      return Response({
        'message':"successfull",
        "data":serializer.data,
        "status": True
      }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




