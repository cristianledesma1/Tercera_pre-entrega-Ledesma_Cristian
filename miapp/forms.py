from django import forms
from .models import Persona, Auto, Direccion

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'edad', 'dni')

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ('marca', 'modelo', 'año')

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ('calle', 'altura', 'localidad')