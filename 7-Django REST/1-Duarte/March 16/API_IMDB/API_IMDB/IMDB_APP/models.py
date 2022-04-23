from django.db import models


class Actor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True, default='')
    birthday = models.DateField()
    description = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ('name',)


class Director(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True, default='')
    birthday = models.DateField()
    description = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ('name',)


class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=True, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    movie_category = models.CharField(max_length=200, blank=True, default='')
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, blank=True, related_name='movies')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
