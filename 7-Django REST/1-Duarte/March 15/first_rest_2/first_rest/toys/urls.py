from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'toys', views.ToyViewSet)

urlpatterns = [
    path('toys/', views.ToyList.as_view(), name="toy-list"),
    path('toys/<int:pk>', views.ToyDetail.as_view(), name="toy-detail")
]

urlpatterns = router.urls
