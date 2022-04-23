from django.urls import path
from . import views

app_name = 'Series'
urlpatterns = [
    path('', views.serie_list, name='serie_list'),
    path('<int:id>', views.serie_detail, name='serie_detail')
]
