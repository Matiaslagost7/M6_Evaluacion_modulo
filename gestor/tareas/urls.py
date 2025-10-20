from django.urls import path
from . import views
from app_login import views as auth_views

app_name = 'tareas'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    
    # Gestión de tareas
    path('tasks/', views.TaskListView, name='task_list'),
    path('tasks/create/', views.TaskCreateView, name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView, name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView, name='task_delete'),
    path('tasks/<int:pk>/', views.TaskDetailView, name='task_detail'),
    
    # URLs de autenticación (alternativas - para compatibilidad)
    path('login/', auth_views.LoginView, name='alt_login'),
    path('register/', auth_views.RegisterView, name='alt_register'),
    path('logout/', auth_views.LogoutView, name='alt_logout'),
]