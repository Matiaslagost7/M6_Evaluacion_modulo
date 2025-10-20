from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def RegisterView(request):
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = request.POST.get('group')
            if group_name:
                group = Group.objects.get(name=group_name)
                user.groups.add(group) # Assign user to the selected group
            login(request, user)  # Log the user in after registration
            return redirect('tareas:index')  # Redirect to a success page.  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        # Validaciones básicas
        if not username:
            messages.error(request, 'Por favor ingresa tu nombre de usuario.')
            return render(request, 'login.html')
        
        if not password:
            messages.error(request, 'Por favor ingresa tu contraseña.')
            return render(request, 'login.html')
        
        # Verificar si el usuario existe
        try:
            user_obj = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            messages.error(request, f'El usuario "{username}" no existe.')
            return render(request, 'login.html')
        
        # Verificar si está activo
        if not user_obj.is_active:
            messages.error(request, 'Tu cuenta está inactiva. Contacta al administrador.')
            return render(request, 'login.html')
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Verificar acceso admin si viene del admin
            next_url = request.GET.get('next', '')
            if '/admin/' in next_url and not user.is_staff:
                messages.error(request, 'No tienes permisos para acceder al área administrativa.')
                return render(request, 'login.html')
            
            login(request, user)
            messages.success(request, f'¡Bienvenido {username}!')
            
            # Redirigir
            if next_url:
                return redirect(next_url)
            else:
                return redirect('tareas:index')
        else:
            messages.error(request, f'Contraseña incorrecta para "{username}".')
    
    return render(request, 'login.html')

def LogoutView(request):
    username = request.user.username if request.user.is_authenticated else None
    
    # Limpiar mensajes previos antes del logout
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Esto consume/limpia los mensajes anteriores
    
    logout(request)
    
    # Agregar solo el mensaje de despedida
    if username:
        messages.success(request, f'¡Hasta luego, {username}! Has cerrado sesión correctamente.')
    else:
        messages.info(request, 'Has cerrado sesión correctamente.')
    
    return redirect('auth:login')
