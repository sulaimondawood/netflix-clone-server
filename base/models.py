from django.db import models
import uuid

class Movie(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  title = models.CharField(max_length=255)
  description = models.TextField()
  image_cover = models.ImageField(upload_to='media/')
  image = models.ImageField(upload_to='media/')
  views = models.IntegerField(default=0)