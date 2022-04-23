from django.contrib import admin
from .models import Movie, MoviesCritic

# Register your models here.

admin.site.register(Movie)
admin.site.register(MoviesCritic)