from django import forms
from .models import Docente

class Docenteform(forms.ModelForm):
    class Meta:
        model= Docente
        fields=[
            'nombre',
            'apellido',
            'edad',
            'email',
            'sexo',
            'cedula',
            'curso_asignado',
            'titulo_Profesion',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'email':'Email',
            'sexo':'Sexo',
            'cedula':'Cedula',
            'curso_asignado':'Curso',
            'titulo_Profesion':'Profesión',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control',}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'cedula':forms.TextInput(attrs={'class':'form-control'}),
            'curso_asignado':forms.TextInput(attrs={'class':'form-control'}),
            'titulo_Profesion':forms.TextInput(attrs={'class':'form-control'}),
        }

