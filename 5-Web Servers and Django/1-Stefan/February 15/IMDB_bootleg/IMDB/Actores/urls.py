from django.urls import path
from . import views

app_name='haruka-tomatsu'
urlpatterns = [
    path('harukatomatsu', views.actores, name='list'),
]