from django.shortcuts import render

# Create your views here.


def whattowatch(request):
    return render(request,
                  'WhatToWatch/whattowatch.html')

def horimiya(request):
    return render(request,
                  'WhatToWatch/horimiya.html')
