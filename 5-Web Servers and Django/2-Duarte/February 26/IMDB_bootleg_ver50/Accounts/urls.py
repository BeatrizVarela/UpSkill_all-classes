from django.urls import path
import django.contrib.auth.views as auth_views
from Accounts import views


app_name = 'Accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]
