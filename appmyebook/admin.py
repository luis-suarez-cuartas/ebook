from django.contrib import admin
from .models import Genero, Idioma, Libro

admin.site.register(Genero)
admin.site.register(Idioma)

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'aprobado']  # Para mostrar el estado de aprobación
    actions = ['aprobar_libros']

    def aprobar_libros(self, request, queryset):
        queryset.update(aprobado=True)
    aprobar_libros.short_description = "Aprobar libros seleccionados"

admin.site.register(Libro, LibroAdmin)
