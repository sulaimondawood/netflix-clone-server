from rest_framework import serializers
from .models import Post,Tag

class PostSerializer(serializers.ModelSerializer):
  # author = 
  class Meta:
    model = Post
    fields = "__all__"

    
class CategoryListSerializer(serializers.Serializer):
  category_name = serializers.CharField(max_length=255)

class TagListSerializer(serializers.ModelSerializer):
  class Meta:
    model= Tag
    fields = "__all__"
