from django.urls import path
from . import views

app_name = 'series'
urlpatterns = [
    path('', views.series_list, name = 'series_list')
]