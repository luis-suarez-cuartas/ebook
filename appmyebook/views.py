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

def index(request):
    return render(request, 'index.html')

def literatura_clasica(request):
    idioma_id_session = request.session.get('idioma_seleccionado', None)
    if idioma_id_session is None:
        idioma_id_session = idioma_id_predeterminado  
        idioma = get_object_or_404(Idioma, pk=idioma_id_session)
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = Libro.objects.filter(genero='Literatura Clásica', idioma=idioma)
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'literatura_clasica.html', context)

def filosofia(request, idioma_id):
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = Libro.objects.filter(genero='Filosofía', idioma=idioma)
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'filosofia.html', context)

def poesia(request, idioma_id):
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = Libro.objects.filter(genero='Poesía', idioma=idioma)
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'poesia.html', context)

def teatro(request, idioma_id):
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = Libro.objects.filter(genero='Teatro', idioma=idioma)
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'teatro.html', context)

def novela(request, idioma_id):
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = Libro.objects.filter(genero='Novela', idioma=idioma)
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'novela.html', context)

def cambiar_idioma(request):
    if request.method == 'POST':
        idioma = request.POST.get('idioma')
        if idioma:
            request.session['idioma_seleccionado'] = idioma
    return redirect(request.META.get('HTTP_REFERER', '/'))



