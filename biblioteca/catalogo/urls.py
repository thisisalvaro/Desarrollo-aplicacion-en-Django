# catalogo/urls.py
from django.urls import path
from .views import pagina_principal, listado_autores, listado_libros, detalles_libro, detalles_autor

urlpatterns = [
    path('', pagina_principal, name='index'),
    path('autores/', listado_autores, name='listado_autores'),
    path('libros/', listado_libros, name='listado_libros'),
    path('libro/<int:pk>/', detalles_libro, name='detalles_libro'),
    path('autor/<int:pk>/', detalles_autor, name='detalles_autor'),
]