from django.shortcuts import render
from django import forms

alarmas = ['5:30', '5:35', '5:40', '5:50']

# Create your views here.

def index(request):
    return render(request, 'alarmas/index.html', {'alarmas':alarmas})

class FNuevaAlarma(forms.Form):
    alarma = forms.CharField(label='nueva alarma')

    snooze=forms.IntegerField(label="repetir",min_value=0,max_value=10)