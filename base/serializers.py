from rest_framework import serializers
from .models import Post,Tag,Category, Comment
from authentication.models import CustomUser

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model= CustomUser
    fields = ('id', 'username', 'first_name', 'last_name')
    extra_kwargs = {
      "password":{
        "write_only":True
      }
    }



class CategoryListSerializer(serializers.ModelSerializer):
  class Meta:
    model= Category
    fields = "__all__"



class TagListSerializer(serializers.ModelSerializer):
  class Meta:
    model= Tag
    fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  category = CategoryListSerializer(many=True)
  tag= TagListSerializer(many=True)
  class Meta:
    model = Post
    fields = ('id', "author", "title", "content",  "comment", 'tag', "category","excerpt","draft_status", "publish_date", "likes","views", "updated_at","created_at")

    

class PostCreateSerializer(serializers.Serializer):

  STATUS_CHOICE = (
    ("DRAFT", "Draft"),
    ("PUBLISHED", "Published")
  )


  id = serializers.UUIDField(read_only=True)
  title = serializers.CharField(max_length=255)
  content = serializers.CharField()
  excerpt =serializers.CharField()
  draft_status =serializers.ChoiceField(choices=STATUS_CHOICE, default="PUBLISHED")
  publish_date = serializers.DateTimeField()
  category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
  tag= serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all() ,many=True)
  likes = serializers.IntegerField()
  comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), many=True)
  views = serializers.IntegerField()
  updated_at = serializers.DateTimeField()
  created_at = serializers.DateTimeField()
