from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from django.contrib.auth.decorators import login_required, permission_required
from .forms import LibroForm, AutorForm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Reserva
from .serializers import AutorSerializer, LibroSerializer, ReservaSerializer

@login_required
def pagina_principal(request):
    return render(request, 'catalogo/index.html')

@permission_required('catalogo.view_libro')
def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/libro_list.html', {'libros': libros})

@permission_required('catalogo.view_autor')
def listado_autores(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/listado_autores.html', {'autores': autores})

@permission_required('catalogo.view_libro')
def detalles_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'catalogo/detalles_libro.html', {'libro': libro})

@permission_required('catalogo.view_autor')
def detalles_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    libros = autor.libros.all()
    return render(request, 'catalogo/detalles_autor.html', {'autor': autor, 'libros': libros})

@permission_required('catalogo.add_libro')
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = LibroForm()
    return render(request, 'catalogo/crear_libro.html', {'form': form})

@permission_required('catalogo.change_libro')
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  # Obtiene el libro o lanza 404
    form = LibroForm(instance=libro)

    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')

    return render(request, 'catalogo/editar_libro.html', {'form': form, 'libro': libro})

@permission_required('catalogo.delete_libro')
def borrar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('pagina_principal')
    return render(request, 'catalogo/borrar_libro.html', {'libro': libro})

@permission_required('catalogo.add_autor')
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = AutorForm()
    return render(request, 'catalogo/crear_autor.html', {'form': form})

@permission_required('catalogo.change_autor')
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

@permission_required('catalogo.delete_autor')
def borrar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('pagina_principal')
    return render(request, 'catalogo/borrar_autor.html', {'autor': autor})

# Vistas para la API REST

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def crear_reserva(self, request):
        libro_id = request.data.get('libro')
        cantidad = request.data.get('cantidad')
        email = request.data.get('email')
        libro = Libro.objects.get(id=libro_id)
        if libro.stock >= int(cantidad):
            libro.stock -= int(cantidad)
            libro.save()
            reserva = Reserva.objects.create(libro=libro, cantidad=cantidad, email=email)
            return Response({'status': 'reserva creada'}, status=201)
        else:
            return Response({'status': 'stock insuficiente'}, status=400)