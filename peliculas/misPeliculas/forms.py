from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        fields = ('titulo', 'director', 'genero')
        model = Pelicula