import django.contrib.auth.views as auth_views

from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('register/', views.register, name='register'),
    path('register_done/', views.register, name='register_done'),
    path('edit/', views.edit, name='edit'),
    path('profile/<int:profile_id>/', views.profile, name='profile'),
]
