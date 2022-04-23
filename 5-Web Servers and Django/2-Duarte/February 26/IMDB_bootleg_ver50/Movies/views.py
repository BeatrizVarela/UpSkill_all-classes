from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from Movies.models import Movie

# Create your views here.


def movie_list(request):
    object_list = Movie.objects.all()
    paginator = Paginator(object_list,3) #numero de objectos por pagina #paginator cria as listas
    page = request.GET.get('page') #devolve a pagina para onde mudámos
    try:
        movies = paginator.page(page) #muda a lista de movies quando muda a pagina
    except PageNotAnInteger:
        movies = paginator.page(1) #quando o numero no url da pagina não é um integer, o servidor devolve a primeira página
    except EmptyPage:
        movies = paginator.page(paginator.num_pages) #devolve a última página do site quando se tenta aceder a uma página não existente
    return render(request, 'Movies/movies.html', {'page':page,'movies':movies}) #chama o .html e cria variaveis para aceder no html

def movie_detail(request,id):
    movie = get_object_or_404(Movie,id=id) #devolver o movie ou entao devolver um 404
    return render(request, 'Movies/details.html', {'movie':movie})
