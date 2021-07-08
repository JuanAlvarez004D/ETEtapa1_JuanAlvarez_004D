from django.urls import path
from .views import Index, ingresar_colaborador, mostrar_colaborador, mod_colaborador, del_colaborador
urlpatterns = [

    path('', Index, name="Index"),
    path('ingresar_colaborador', ingresar_colaborador, name="ingresar_colaborador"),
    path('mostrar_colaborador', mostrar_colaborador, name="mostrar_colaborador"),
    path('mod_colaborador/<id>', mod_colaborador, name="mod_colaborador"),
    path('del_colaborador<id>', del_colaborador, name="del_colaborador")

    #metodos
]

