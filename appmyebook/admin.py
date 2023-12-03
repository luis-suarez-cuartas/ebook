from django.contrib import admin
from .models import Genero, Idioma, Libro
from django.utils.translation import gettext_lazy as _

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'aprobado']
    actions = ['aprobar_libros']

    def aprobar_libros(self, request, queryset):
        queryset.update(aprobado=True)
    aprobar_libros.short_description = _("Aprobar libros seleccionados")

admin.site.register(Libro, LibroAdmin)

