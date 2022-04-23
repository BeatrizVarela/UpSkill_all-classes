from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from Staff.models import Staff

# Create your views here.

def staff_list(request):
    object_list = Staff.objects.all()
    paginator = Paginator(object_list,3) #numero de objectos por pagina #paginator cria as listas
    page = request.GET.get('page') #devolve a pagina para onde mudámos
    try:
        staff = paginator.page(page) #muda a lista de staff quando muda a pagina
    except PageNotAnInteger:
        staff = paginator.page(1) #quando o numero no url da pagina não é um integer, o servidor devolve a primeira página
    except EmptyPage:
        staff = paginator.page(paginator.num_pages) #devolve a última página do site quando se tenta aceder a uma página não existente
    return render(request, 'Staff/staff.html', {'page':page,'staff':staff}) #chama o .html e cria variaveis para aceder no html


def staff_detail(request,id):
    staff = get_object_or_404(Staff,id=id)
    return render(request, 'Staff/details.html', {'staff':staff})
