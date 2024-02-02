from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post

class Postist(APIView):
  permission_classes = [AllowAny]

  def get(self, request):
    objs = Post.objects.all()
      
