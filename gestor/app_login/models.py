from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ('ver_tareas', 'Puede ver las tareas'),
            ('editar_tareas', 'Puede editar las tareas'),
            ('eliminar_tareas', 'Puede eliminar las tareas'),
            ('crear_tareas', 'Puede crear tareas'),
        ]
