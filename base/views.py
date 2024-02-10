from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

 

class PostCreateList(APIView):
  
  def get(self, request):
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True)

    return Response({
      "data":serializer.data,
      "message": "succesfull",
      "status": True
    }, status=status.HTTP_200_OK)



# class PostCreateList(generics.ListCreateAPIView):
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer
#   permission_classes = [IsAuthenticatedOrReadOnly]

#   def list(self, request):
#     queryset = self.ge

  
#   # def perform_create(self, serializer):
#   #   # instance = se
#   #   pass