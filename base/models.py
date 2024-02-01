from django.db import models
import uuid
from django.conf import settings

CustomUser = settings.AUTH_USER_MODEL

class Movie(models.Model):

  GENRE_CHOICES =[
    ("ACTION", 'Action'),
    ("COMEDY", "Comedy"),
    ("THRILLER", 'Thriller'),
    ("DRAMA", 'Drama'),
    ("ROMANCE", 'Romance'),
    ("SCIFI", 'Sci-Fi'),
    ("HORROR", 'Horror'),
  ]

  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  title = models.CharField(max_length=255)
  description = models.TextField()
  image_cover = models.ImageField(upload_to='media/')
  image = models.ImageField(upload_to='media/')
  views = models.IntegerField(default=0)
  video = models.FileField()
  ratings = models.FloatField()
  release_date = models.DateField()
  genres = models.CharField(choices=GENRE_CHOICES, max_length=25, default='ACTION')
  

class Post(models.Model):

  id = models.UUIDField(default=uuid.uuid4, unique=True)
  title = models.CharField(max_length=255, blank=True)
  content = models.TextField()
  author= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  excerpt =models.TextField()
  # draft_status =
  publish_date = models.DateTimeField(auto_now=True)
  # category = models.

  def __str__(self):
    return self.title


class Category(models.Model):
  category_name = models.CharField(max_length=255)

  def __str__(self):
    return self.name
  
class Tags(models.Model):
  
  tag_name = models.CharField(max_length=255)

  def __str__(self):
    return self.tag_name