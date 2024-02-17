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
  title = serializers.CharField(max_length=255)
  content = serializers.CharField(required=False, allow_blank=True)
  excerpt =serializers.CharField(required=False, allow_blank=True)
  draft_status =serializers.ChoiceField(choices=STATUS_CHOICE, default="DRAFT")
  category = serializers.PrimaryKeyRelatedField(required=False, queryset=Category.objects.all(), many=True)
  tag= serializers.PrimaryKeyRelatedField(required=False, queryset=Tag.objects.all() ,many=True)


  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.content = validated_data.get('content', instance.content)
    instance.excerpt = validated_data.get('excerpt', instance.excerpt)
    instance.draft_status = validated_data.get('draft_status', instance.draft_status)

    if "tag" in validated_data:
      instance.tag.set(validated_data["tag"])

    if "category" in validated_data:
      instance.category.set(validated_data["category"])
    # Incorrect implemmentatio
    # instance.tag = validated_data.get('tag', instance.tag)
    # instance.category = validated_data.get('category', instance.category)
    # Incorrect implemmentatio
    instance.save()
    return instance


  def create(self, validated_data):
    title = validated_data.get('title')
    content = validated_data.get('content')
    # author = self.context['request']

    if content is None:
      content = title
      
    return Post.objects.create(**validated_data)
    # return Post.objects.create(author=author, content= content, **validated_data)
  
