from django.urls import path, include
from .views import index, post_list, post_detail, PostListView

app_name = "blog"
urlpatterns = [
    path('', index, name="index"),
    path('posts', PostListView.as_view(), name="list"),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>', post_detail, name="detail")
]