from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class MovieList(APIView):
  permission_classes = AllowAny

  def get(self, request):
    pass
