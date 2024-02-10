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
      "message": "successfull",
      "status": True
    }, status=status.HTTP_200_OK)

  
  def post(self, request):
    title = request.data.get('title')
    content = request.data.get('content')
    excerpt = request.data.get('excerpt')
    draft_status = request.data.get('draft_status')
    tag = request.data.get('tag')
    category = request.data.get('category')



