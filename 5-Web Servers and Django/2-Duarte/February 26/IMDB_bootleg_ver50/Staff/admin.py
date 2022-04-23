from django.contrib import admin
from .models import Staff,Actor,Director,Writer

# Register your models here.

admin.site.register(Staff)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)