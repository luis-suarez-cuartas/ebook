from django.utils import timezone
from django.db import models
 
class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    

class Idioma(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField (Un id).
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    isbn = models.CharField(max_length=8)
    descripcion = models.TextField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE) # Un libro solo puede tener un género
    idioma = models.ManyToManyField(Idioma) # Un libro puede estar en varios idiomas
    imagen = models.ImageField(upload_to='', null=True, blank=True) # Campo para la imagen del libro
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo




   