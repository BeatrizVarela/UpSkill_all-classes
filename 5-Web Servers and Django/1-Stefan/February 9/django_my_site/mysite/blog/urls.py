from django.urls import path
from . import views
from .views import post_by_year, post_by_month, post_by_day

app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    path('search', views.search, name = 'search'),
    path('<slug:tag_slug>', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail'),
    path('posts/<int:year>', post_by_year, name="by_year"),
    path('posts/<int:year>/<int:month>', post_by_month, name="by_month"),
    path('posts/<int:year>/<int:month>/<int:day>', post_by_day, name="by_day")
]

# tudo que é estático convem estar em primeiro