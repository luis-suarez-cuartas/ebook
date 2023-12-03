from django.db import models
from django.utils.translation import gettext_lazy as _

class Genero(models.Model):
    nombre = models.CharField(_("nombre"), max_length=100)
    descripcion = models.TextField(_("descripcion"))

    def __str__(self):
        return self.nombre
    
class Idioma(models.Model):
    nombre = models.CharField(_("nombre"), max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(_("titulo"), max_length=100)
    autor = models.CharField(_("autor"), max_length=50)
    isbn = models.CharField(_("isbn"), max_length=8)
    descripcion = models.TextField(_("descripcion"))
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name=_("genero")) # Un libro solo puede tener un género
    idioma = models.ManyToManyField(Idioma, verbose_name=_("idioma")) # Un libro puede estar en varios idiomas
    imagen = models.ImageField(upload_to='', null=True, blank=True, verbose_name=_("imagen")) # Campo para la imagen del libro
    fecha_creacion = models.DateTimeField(_("fecha de creación"), auto_now_add=True)
    aprobado = models.BooleanField(_("aprobado"), default=False)

    def __str__(self):
        return self.titulo





   