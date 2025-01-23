# catalogo/views.py
from django.shortcuts import render, get_object_or_404
from .models import Autor, Libro

def pagina_principal(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/index.html', {'libros': libros})

def listado_autores(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/listado_autores.html', {'autores': autores})

def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/libro_list.html', {'libros': libros})

def detalles_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'catalogo/detalles_libro.html', {'libro': libro})

def detalles_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    libros = autor.libros.all()
    return render(request, 'catalogo/detalles_autor.html', {'autor': autor, 'libros': libros})