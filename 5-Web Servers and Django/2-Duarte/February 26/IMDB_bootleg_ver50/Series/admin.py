from django.contrib import admin
from .models import Series,Episode,SeriesCritic

# Register your models here.

admin.site.register(Series)
admin.site.register(Episode)
admin.site.register(SeriesCritic)
