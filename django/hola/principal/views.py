from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.

def holaDjango(request):
    return HttpResponse("Hola Django!")