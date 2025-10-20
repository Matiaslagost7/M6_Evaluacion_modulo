from django import forms

class TareaForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Título de la Tarea')
    descripcion = forms.CharField(label='Descripción', required=False, widget=forms.Textarea)
    fecha_vencimiento = forms.DateTimeField(label='Fecha de Vencimiento')
    completada = forms.BooleanField(label='Marcar como completada', required=False)