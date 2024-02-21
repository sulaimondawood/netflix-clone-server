from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Post, Tag, Category
from .serializers import PostSerializer, PostCreateSerializer,TagListSerializer, CategoryListSerializer

from base.permissions import CreatedBy
 
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
  # permission_classes= [IsAuthenticatedOrReadOnly ]

  def get(self, request):
    qs = Post.objects.all()
    serializer = PostSerializer(qs, many=True)

    return Response({
      "data":serializer.data,
      "message": "successfull",
      "status": True
    }, status=status.HTTP_200_OK)

  
  def post(self, request):
    # serializer = PostCreateSerializer(data= request.data, context={"request", request})
    serializer = PostCreateSerializer(data= request.data, context={"request", request})
    if serializer.is_valid(raise_exception=True):
      # serializer.save(author = request.user)
      serializer.save()
      return Response({
        'message':"successfull",
        "data":serializer.data,
        "status": True
      }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDeleteEditRetrieve(APIView):
  permission_classes = [CreatedBy]

  def get(self, request, pk):
    queryset = Post.objects.filter(id = pk)
    serializer = PostSerializer(queryset, many=True)
    return Response({
      "data":serializer.data,
      "message": "successfull",
      "status": True
    }, status=status.HTTP_200_OK)


  def put(self, request, pk):
    queryset = Post.objects.get(id=pk)
    serializer= PostCreateSerializer(queryset, data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response({
      'message':"successfull",
      "data": serializer.data,
      "status": True,
      }, status=status.HTTP_200_OK)

    return Response({"error": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


  def delete(self, request, pk):
    queryset= Post.objects.get(id=pk)
    queryset.delete()

    return Response({"message": "successfull",
                     "status": True}, status=status.HTTP_204_NO_CONTENT)
