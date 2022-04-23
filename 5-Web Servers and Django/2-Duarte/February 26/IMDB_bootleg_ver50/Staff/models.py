from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Staff(models.Model):
    GENDER_CHOICES = (('male','Male'),
                      ('female','Female'),
                      ('other','Other'))

    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30,choices=GENDER_CHOICES)
    description = models.TextField()
    photos = models.ImageField(upload_to='staff/')
    roles = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Staff:staff_detail',args=[self.id])

class Actor(models.Model):
    person = models.ForeignKey(Staff,on_delete=models.CASCADE, related_name='actor')

    def __str__(self):
        return self.person.name

class Director(models.Model):
    person = models.ForeignKey(Staff,on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return self.person.name

class Writer(models.Model):
    person = models.ForeignKey(Staff,on_delete=models.CASCADE, related_name='writer')

    def __str__(self):
        return self.person.name
