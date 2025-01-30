from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import LibroForm, AutorForm

def pagina_principal(request):
    return render(request, 'catalogo/index.html')

def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/libro_list.html', {'libros': libros})

def listado_autores(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/listado_autores.html', {'autores': autores})

def detalles_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'catalogo/detalles_libro.html', {'libro': libro})

def detalles_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    libros = autor.libros.all()
    return render(request, 'catalogo/detalles_autor.html', {'autor': autor, 'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = LibroForm()
    return render(request, 'catalogo/crear_libro.html', {'form': form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'catalogo/editar_libro.html', {'form': form})

def borrar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('pagina_principal')
    return render(request, 'catalogo/borrar_libro.html', {'libro': libro})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = AutorForm()
    return render(request, 'catalogo/crear_autor.html', {'form': form})

def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'catalogo/editar_autor.html', {'form': form})

def borrar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('pagina_principal')
    return render(request, 'catalogo/borrar_autor.html', {'autor': autor})