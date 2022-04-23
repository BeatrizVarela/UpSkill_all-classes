from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.views.generic import ListView
from taggit.models import Tag

from .forms import CommentForm
from .models import Post # o . diz que é na directoria actual


def search(request):
    #obter os argumentos do get
    # o GET é o dicionario da request
    query = request.GET.get("query")
    if query:
        results = Post.published.filter(Q(title__contains=query) | Q(body__contains=query))
    else:
        results = None

    #title_query = Post.published.filter(title__contains=query)# para ver se a palavra está algures no título
    #body_query = Post.published.filter(body__contains=query)
    #results = title_query.union(body_query)

    return render(request,
                  'blog/post/search.html',
                  {'results': results})


@login_required
def post_list(request, tag_slug=None):

    num_visits = int(request.COOKIES.get('num_visits', 0))
    num_visits += 1

    object_list = Post.published.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

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
    response = render(request,
                 'blog/post/list.html',
                 {'page': page,
                  'posts': posts,
                  'tag': tag},
    )

    response.set_cookie('num_visits', num_visits)
    return response


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST) # prepopular formulario com os dados do comentario
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
            return redirect(post)
    elif request.method == 'GET':
        comment_form = CommentForm() # isto gera o formulario

    post_tags_ids = post.tags.values_list('id', flat=True) # devolve uma lista de tuplos
    # posts com pelo menos uma das tags em comum
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                    .exclude(id=post.id)
    # same_tags é uma nova variavel pq é uma 'função' do annotate
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    # raise RuntimeError(similar_posts, post_tags_ids)
    return render(request,
                  'blog/post/detail.html',
                  {
                      'post': post,
                      'comment_form': comment_form,
                      'new_comment': new_comment,
                      'similar_posts': similar_posts,
                   })


def post_by_year(request,year):
    object_list = Post.published.filter(publish__year=year)
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
    return render(request, "blog/post/list.html", {"posts": posts})


def post_by_month(request,year,month):
    object_list = Post.published.filter(publish__year=year, publish__month=month)
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

    return render(request, "blog/post/list.html", {"posts": posts})


def post_by_day(request,year,month,day):
    object_list = Post.published.filter(publish__year=year, publish__month=month, publish__day=day)
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

    return render(request, "blog/post/list.html", {"posts": posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    # cria um objecto paginator
    paginate_by = 3
    template_name = 'blog/post/list.html'

