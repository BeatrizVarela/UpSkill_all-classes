from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from Staff.models import Actor, Director, Writer

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    director = models.ManyToManyField(Director, related_name='movies')
    writer = models.ManyToManyField(Writer, related_name='movies')
    duration = models.CharField(max_length=20)
    images = models.ImageField(upload_to='movies/')
    rating = models.CharField(max_length=30)
    evaluation = models.FloatField(validators=
                                     [MinValueValidator(0),
                                     MaxValueValidator(10)])
    release_date = models.DateField()
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Movies:movie_detail',args=[self.id])

class MoviesCritic(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='movie_critics')
    title = models.CharField(max_length=100)
    critic = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    evaluation = models.IntegerField(validators=
                                     [MinValueValidator(0),
                                     MaxValueValidator(10)])
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='critics')

    def __str__(self):
        return 'Comment from', self.user.username, 'of', self.movie.name
