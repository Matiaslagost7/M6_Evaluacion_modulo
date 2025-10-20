from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Gestor_tareas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField()
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-fecha_creacion']