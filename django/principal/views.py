from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def holaDjango(request):
    return HttpResponse("Hola Django!")


def pepe(request):
    return HttpResponse('Hola pepe')

def holatu(request, nombre):
    return HttpResponse(f'Hola {nombre.capitalize()}')

def indice(request):
    return render(request, 'principal/index.html')

def indiceparam(request, nombre):
    return render(request, 'principal/saludo.html', {
        'nombre': nombre.capitalize()
    })
    