from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'actors', views.ActorsViewSet)
router.register(r'directors', views.DirectorsViewSet)
router.register(r'movies', views.MoviesViewSet)

urlpatterns = router.urls
