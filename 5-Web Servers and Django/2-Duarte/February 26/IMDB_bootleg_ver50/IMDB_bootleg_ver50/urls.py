"""IMDB_bootleg_ver50 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Homepage.urls', namespace='Homepage')),
    path('accounts/', include('Accounts.urls', namespace='Accounts')),
    path('movies/', include('Movies.urls', namespace='Movies')),
    path('series/', include('Series.urls', namespace='Series')),
    path('staff/', include('Staff.urls', namespace='Staff'))
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #a boa pratica é usar cdn
