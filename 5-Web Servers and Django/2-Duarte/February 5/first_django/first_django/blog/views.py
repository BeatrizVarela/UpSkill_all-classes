from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post
from django.views.generic import ListView


def index(request):
    return HttpResponse("Torradas") # render(request, "blog/base.html")

'''
def post_list(request):
    post_list = Post.published.all()
    return render(request, "blog/post/list.html", {"post": post_list})
'''

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, publish__day=day, publish__month=month, publish__year=year)
    return render(request, "blog/post/detail.html", {"post": post})

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                 'blog/post/detail.html',
                 {'page': page,
                  'posts': posts})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'