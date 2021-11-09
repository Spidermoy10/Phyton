from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

alarmas = ['5:30', '5:35', '5:40', '5:50']

# Create your views here.

def index(request):
    return render(request, 'alarmas/index.html', {'alarmas':alarmas})

def v2(request):
    if request.method == 'POST':
        form = FNuevaAlarma(request.POST) #vacio -> nuevo; lleno -> toma valores actuales
        if form.is_valid():
            alarma = form.cleaned_data['alarma']
            alarmas.append(alarma)
            return HttpResponseRedirect(reverse('alarmas:index'))
        else:
            return render(request, 'alarmas/nueva.html', {'cont_form': form}) #reverse?
    else:
        return render(request, 'larmas/nueva.html', {'cont_form': FNuevaAlarma()}) #reverse?


class FNuevaAlarma(forms.Form):
    alarma = forms.CharField(label='nueva alarma')

   # snooze=forms.IntegerField(label="repetir",min_value=0,max_value=10)