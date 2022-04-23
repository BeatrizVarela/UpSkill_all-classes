from django.shortcuts import render

# Create your views here.

def actores(request):
    return render(request,
                  'Actores/actores.html')
