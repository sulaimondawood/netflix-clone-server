from django.db import models
import uuid

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
  