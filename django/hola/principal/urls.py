from django.urls import path
from.import views

urlpatterns=[
    path("",views.holaDjango,name="holaDjango"),
    path("",views.holaPepe, name="HolaPepe"),
    path('<str:nombre>',views.holaTu, name='holaTu')
]