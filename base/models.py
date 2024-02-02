from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone

CustomUser = settings.AUTH_USER_MODEL

class Comment(models.Model):

  comment = models.TextField()
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
  title = models.CharField(max_length=255, blank=True)
  content = models.TextField()
  author= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  excerpt =models.TextField()
  draft_status =models.CharField(max_length=255, choices=STATUS_CHOICE, default='PUBLISHED')
  publish_date = models.DateTimeField(auto_now=True)
  category = models.ManyToManyField('Category', blank=True)
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
  
