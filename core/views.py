from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

#Paginas
def Index(request):
    return render(request, 'index.html')

def ingresar_colaborador(request):
    datos = {
        'form': UsuarioForm()
    }

    if request.method == 'POST': 
        usuario = UsuarioForm(request.POST, files=request.FILES)
        if usuario.is_valid():
            usuario.save()         
            return redirect('Index')
    else: 
        usuario = UsuarioForm()

    return render(request, 'core/ingresar_colaborador.html', {'usuario': usuario})

def mostrar_colaborador(request):
    usuario=Usuario.objects.all()
    return render(request, 'core/mostrar_colaborador.html', context={'usuarios':usuario})

def mod_colaborador(request, id):
    usuario = get_object_or_404(Usuario, RutUsuario=id)
    datos ={
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance = usuario, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar_colaborador')
        datos["form"] = formulario

    return render(request, 'core/mod_colaborador.html', datos)

def del_colaborador(request,id):
    usuario = get_object_or_404(Usuario, RutUsuario=id)
    usuario.delete()
    return redirect('mostrar_colaborador')
