from django import forms
from .models import Docente

class Docenteform(forms.ModelForm):
    class Meta:
        model= Docente
        fields=('nombre','apellido','edad','email','sexo','curso_asignado','titulo_Profesion')

