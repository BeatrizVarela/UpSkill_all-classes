from django.shortcuts import render
from .models import Series

# Create your views here.

def series_list(request):
    series = Series.objects.all()
    print(series)
    return render(request,'Series/series.html',{'series':series})
