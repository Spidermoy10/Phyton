from django.urls import path
from . import views

urlpatterns = [
    
    path('indice', views.indice, name='indice'),
    path('indice/<str:nombre>', views.indiceparam, name='indice'),
    
   
    ]