from django.urls import path
from . import views

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
]