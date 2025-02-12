from django import forms
from .models import Libro, Autor

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'stock','genero','anio_publicacion' ] 

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos']
