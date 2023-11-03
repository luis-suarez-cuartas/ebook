from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Libro, Genero, Idioma

#devuelve los datos de un libro
def show_libro(request, libro_id):
    libro = get_object_or_404(libro, pk=libro_id)
    context = {'libro': libro }
    return render(request, 'libro.html', context)
    
# devuelve los libros de un genero y un idioma
def index_libro(request, genero_id, idioma_id):
    genero = get_object_or_404(Genero, pk=genero_id)
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = get_list_or_404(Libro, genero=genero, idioma=idioma)
    context = {'libros': libros}
    return render(request, 'generoIdioma.html', context) #TODO generoIdioma.html no existe