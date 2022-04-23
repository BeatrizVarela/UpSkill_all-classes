from django.contrib import admin
from . import models

admin.site.register(models.Drone)
admin.site.register(models.DroneCategory)
admin.site.register(models.Pilot)
admin.site.register(models.Competition)
