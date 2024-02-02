from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
  permission_classes = [AllowAny]

  def get(self, request):
    query_set = Post.objects.all()
    serializer = PostSerializer(query_set, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
    