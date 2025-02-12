from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import pagina_principal, listado_libros, listado_autores, detalles_libro, detalles_autor, crear_libro, editar_libro, borrar_libro, crear_autor, editar_autor, borrar_autor, AutorViewSet, LibroViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('autores/', listado_autores, name='listado_autores'),
    path('libros/', listado_libros, name='listado_libros'),
    path('libro/<int:pk>/', detalles_libro, name='detalles_libro'),
    path('autor/<int:pk>/', detalles_autor, name='detalles_autor'),
    path('libro/crear/', crear_libro, name='crear_libro'),
    path('libro/editar/<int:pk>/', editar_libro, name='editar_libro'),
    path('libro/borrar/<int:pk>/', borrar_libro, name='borrar_libro'),
    path('autor/crear/', crear_autor, name='crear_autor'),
    path('autor/editar/<int:pk>/', editar_autor, name='editar_autor'),
    path('autor/borrar/<int:pk>/', borrar_autor, name='borrar_autor'),
    path('api/', include(router.urls)),
]