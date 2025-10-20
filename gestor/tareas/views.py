from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import models
from django.http import Http404
from .models import Gestor_tareas
from .forms import TareaForm
from app_login.mixins import verificar_login_permiso

def get_tarea_or_404(request, pk):
    """
    Obtiene una tarea que pertenezca al usuario autenticado o devuelve 404.
    """
    try:
        return get_object_or_404(Gestor_tareas, id=pk, usuario=request.user)
    except:
        raise Http404("La tarea no existe o no tienes permisos para acceder a ella.")

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        tareas = Gestor_tareas.objects.filter(usuario=request.user)
    else:
        tareas = []
    return render(request, 'index.html', {'tareas': tareas})

def TaskListView(request):
    """Vista para listar todas las tareas del usuario autenticado."""
    resultado = verificar_login_permiso(request, 'app_login.ver_tareas')
    if resultado:
        return resultado

    tareas = Gestor_tareas.objects.filter(usuario=request.user)
    return render(request, 'lista_tarea.html', {'tareas': tareas})

def TaskCreateView(request):
    """Vista para crear una nueva tarea usando Django Forms."""
    resultado = verificar_login_permiso(request, 'app_login.crear_tareas')
    if resultado:
        return resultado

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            # Crear la tarea con los datos validados del formulario y asignar al usuario actual
            Gestor_tareas.objects.create(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                fecha_vencimiento=form.cleaned_data['fecha_vencimiento'],
                completada=form.cleaned_data['completada'],
                usuario=request.user
            )
            messages.success(request, f'Tarea "{form.cleaned_data["nombre"]}" creada exitosamente.')
            return redirect('tareas:task_list')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = TareaForm()

    return render(request, 'crear_tarea.html', {'form': form})

def TaskUpdateView(request, pk):
    """Vista para editar una tarea existente del usuario autenticado usando Django Forms."""
    resultado = verificar_login_permiso(request, 'app_login.editar_tareas')
    if resultado:
        return resultado

    tarea = get_tarea_or_404(request, pk)

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            # Actualizar la tarea con los datos validados del formulario
            tarea.nombre = form.cleaned_data['nombre']
            tarea.descripcion = form.cleaned_data['descripcion']
            tarea.fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
            tarea.completada = form.cleaned_data['completada']
            tarea.save()

            messages.success(request, f'Tarea "{tarea.nombre}" actualizada exitosamente.')
            return redirect('tareas:task_list')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        # Pre-llenar el formulario con los datos actuales de la tarea
        form = TareaForm(initial={
            'nombre': tarea.nombre,
            'descripcion': tarea.descripcion,
            'fecha_vencimiento': tarea.fecha_vencimiento,
            'completada': tarea.completada
        })

    return render(request, 'editar_tarea.html', {'form': form, 'tarea': tarea})

def TaskDeleteView(request, pk):
    """Vista para eliminar una tarea existente del usuario autenticado."""
    resultado = verificar_login_permiso(request, 'app_login.eliminar_tareas')
    if resultado:
        return resultado

    tarea = get_tarea_or_404(request, pk)
    
    if request.method == 'POST':
        nombre_tarea = request.POST.get('nombre_tarea', '')
        confirmacion = request.POST.get('confirmacion', '')
        
        if confirmacion == nombre_tarea:
            tarea.delete()
            messages.success(request, f'Tarea "{nombre_tarea}" eliminada exitosamente.')
            return redirect('tareas:task_list')
        else:
            messages.error(request, 'La confirmación no coincide con el nombre de la tarea.')
    
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})

def TaskDetailView(request, pk):
    """Vista para mostrar detalles de una tarea específica del usuario autenticado."""
    resultado = verificar_login_permiso(request, 'app_login.ver_tareas')
    if resultado:
        return resultado

    tarea = get_tarea_or_404(request, pk)
    return render(request, 'detalle_tarea.html', {'tarea': tarea})
