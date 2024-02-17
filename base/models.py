from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone

CustomUser = settings.AUTH_USER_MODEL

class Comment(models.Model):

  comment = models.TextField(blank=True, null=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(default=timezone.now)


  def __str__(self):
    return self.comment[:20]


class Post(models.Model):

  STATUS_CHOICE = (
    ("DRAFT", "Draft"),
    ("PUBLISHED", "Published")
  )

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
  author= models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
  title = models.CharField(max_length=255, blank=True, null=True)
  content = models.TextField()
  excerpt =models.TextField()
  draft_status =models.CharField(max_length=255, choices=STATUS_CHOICE, default='DRAFT')
  publish_date = models.DateTimeField(auto_now=True)
  category = models.ManyToManyField('Category')
  tag= models.ManyToManyField('Tag')
  likes = models.IntegerField(default=0)
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
  views = models.IntegerField(default=0, blank=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(default=timezone.now )

  class Meta:
    ordering = ('-updated_at', '-created_at')

  def __str__(self):
    return self.title


class Category(models.Model):
  category_name = models.CharField(max_length=255)

  def __str__(self):
    return self.category_name
  
  
class Tag(models.Model):
  tag_name = models.CharField(max_length=255)

  def __str__(self):
    return self.tag_name
  



