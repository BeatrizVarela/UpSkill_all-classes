from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Series(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    actores = models.CharField(max_length=50)
    # actores = models.ManyToManyField(Actores, related_name='series')
    director = models.CharField(max_length=50)
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    images = models.ImageField(upload_to='series/')
    rating = models.CharField(max_length=30)
    evaluation = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name