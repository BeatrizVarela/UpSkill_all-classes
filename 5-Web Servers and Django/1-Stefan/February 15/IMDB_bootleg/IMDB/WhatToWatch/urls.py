from django.urls import path
from . import views

app_name='what-to-watch'
urlpatterns = [
    path('', views.whattowatch, name='list'),
    path('horimiya', views.horimiya, name='horimiya'),
]
