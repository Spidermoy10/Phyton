from django.urls import path
from.import views

urlpatterns=[
    path('indice',views.indice, name="HolaIndice"),
    path("",views.holaDjango,name="holaDjango"),
    path('indice/str:nombre',views.indiceParam, name='indiceParam'),
    path('pepe',views.pepe, name="HolaPepe"),
    path('<str:nombre>',views.holaTu, name='holaTu'),
    path('indice',views.indice, name='indice')
]