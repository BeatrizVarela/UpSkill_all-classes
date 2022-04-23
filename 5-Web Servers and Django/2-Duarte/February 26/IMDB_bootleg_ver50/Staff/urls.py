from django.urls import path
from . import views

app_name = 'Staff'
urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('<int:id>', views.staff_detail, name='staff_detail')
]
