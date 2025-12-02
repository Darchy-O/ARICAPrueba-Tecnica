# usuarios/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        Usuario.objects.create(
            Rut=request.POST['rut'],
            Nombre=request.POST['nombre'],
            Apellido=request.POST['apellido']
        )
        return redirect('listar')
    return render(request, 'crear.html')

def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, Id_user=id)
    if request.method == 'POST':
        usuario.Rut = request.POST['rut']
        usuario.Nombre = request.POST['nombre']
        usuario.Apellido = request.POST['apellido']
        usuario.save()
        return redirect('listar')
    return render(request, 'actualizar.html', {'usuario': usuario})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, Id_user=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar')
    return render(request, 'eliminar.html', {'usuario': usuario})