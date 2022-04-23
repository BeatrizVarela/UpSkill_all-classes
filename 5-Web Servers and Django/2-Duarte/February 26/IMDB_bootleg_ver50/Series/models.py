from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from Staff.models import Actor, Director, Writer
from django.contrib.auth.models import User

# Create your models here.

class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='series')
    director = models.ManyToManyField(Director, related_name='series')
    writer = models.ManyToManyField(Writer, related_name='series')
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    images = models.ImageField(upload_to='series/')
    rating = models.CharField(max_length=30)
    evaluation = models.FloatField(validators=
                                     [MinValueValidator(0),
                                     MaxValueValidator(10)])
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Series:serie_detail',args=[self.id])

class Episode(models.Model):
    series = models.ForeignKey(Series,on_delete=models.CASCADE,related_name='eps')
    name = models.CharField(max_length=100)
    season = models.IntegerField()
    number = models.IntegerField()
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='episodes')
    director = models.ManyToManyField(Director, related_name='episodes')
    writer = models.ManyToManyField(Writer, related_name='episodes')
    images = models.ImageField(upload_to='series/episodes/')
    rating = models.CharField(max_length=30)
    evaluation = models.FloatField(validators=
                                     [MinValueValidator(0),
                                     MaxValueValidator(10)])
    release_date = models.DateField()


    def __str__(self):
        return f'{self.series.name}, Season {self.season} Episode {self.number}'

    class Meta:
        unique_together = (('series','season','number'),)

class SeriesCritic(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='series_critics')
    title = models.CharField(max_length=100)
    critic = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    evaluation = models.IntegerField(validators=
                                     [MinValueValidator(0),
                                     MaxValueValidator(10)])
    serie = models.ForeignKey(Series,on_delete=models.CASCADE,related_name='critics')

    def __str__(self):
        return 'Comment from', self.user.username, 'of', self.serie.name
