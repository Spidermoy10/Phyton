from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indice(request):
    return render(request, 'viernes/dia2.html')

def indiceparam(request, nombre):
    return render(request, 'viernes/dia.html', {
        'nombre': nombre.capitalize()
    })
    