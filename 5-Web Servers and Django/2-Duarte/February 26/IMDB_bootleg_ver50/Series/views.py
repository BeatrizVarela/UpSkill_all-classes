from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from Series.models import Series

# Create your views here.

def serie_list(request):
    object_list = Series.objects.all()
    paginator = Paginator(object_list,3) #numero de objectos por pagina #paginator cria as listas
    page = request.GET.get('page') #devolve a pagina para onde mudámos
    try:
        series = paginator.page(page) #muda a lista de series quando muda a pagina
    except PageNotAnInteger:
        series = paginator.page(1) #quando o numero no url da pagina não é um integer, o servidor devolve a primeira página
    except EmptyPage:
        series = paginator.page(paginator.num_pages) #devolve a última página do site quando se tenta aceder a uma página não existente
    return render(request, 'Series/series.html', {'page':page,'series':series}) #chama o .html e cria variaveis para aceder no html

def serie_detail(request,id):
    serie = get_object_or_404(Series,id=id) #devolver a serie ou entao devolver um 404
    return render(request, 'Series/details.html', {'serie':serie})
