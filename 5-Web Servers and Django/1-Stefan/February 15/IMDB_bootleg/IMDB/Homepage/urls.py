from django.urls import path
from . import views

app_name='homepage'
urlpatterns = [
    path('', views.index),
    path('what-to-watch/', views.whattowatch),
]
