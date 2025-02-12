from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    isbn = models.CharField(max_length=13, unique=True)
    stock = models.PositiveIntegerField(default=0)
    genero = models.CharField(max_length=100, blank=True, null=True)
    anio_publicacion = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    email = models.EmailField()
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='reservas')
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva de {self.cantidad} libros para {self.email}"