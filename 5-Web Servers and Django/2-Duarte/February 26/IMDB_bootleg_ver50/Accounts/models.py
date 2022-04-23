from django.db import models
from django.conf import settings
from Staff.models import Actor, Director, Writer
from Series.models import Series
from Movies.models import Movie

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    photo = models.ImageField(upload_to='profile/',blank=True)
    description = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    favorite_movies = models.ManyToManyField(Movie, related_name='movies', blank=True)
    favorite_series = models.ManyToManyField(Series, related_name='series', blank=True)
    favorite_actors = models.ManyToManyField(Actor, related_name='actor', blank=True)
    favorite_directors = models.ManyToManyField(Director, related_name='director', blank=True)
    favorite_writers = models.ManyToManyField(Writer, related_name='writer', blank=True)

    def __str__(self):
        return self.user.username
