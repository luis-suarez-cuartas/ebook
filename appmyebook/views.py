from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Libro, Genero, Idioma
from django.shortcuts import redirect

#devuelve los datos de un libro
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    context = {'libro': libro }
    return render(request, 'detalle_libro.html', context)
    
# devuelve los libros de un genero y un idioma
def index_libro(request, genero_id, idioma_id):
    genero = get_object_or_404(Genero, pk=genero_id)
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = get_list_or_404(Libro, genero=genero, idioma=idioma)
    context = {'libros': libros}
    return render(request, 'generoIdioma.html', context) #TODO generoIdioma.html no existe

def index(request):
    return render(request, 'index.html')

def literaturaClasica(request):
    idioma_nombre = request.session.get('idioma_seleccionado', None)
    if idioma_nombre is None:
        idioma_nombre = 'Castellano'
    idioma = get_object_or_404(Idioma, nombre=idioma_nombre)
    libros = Libro.objects.filter(genero__nombre='Literatura Clásica', idioma=idioma).order_by('-fecha_creacion')
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'literaturaClasica.html', context)

def filosofia(request):
    idioma_nombre = request.session.get('idioma_seleccionado', None)
    if idioma_nombre is None:
        idioma_nombre = 'Castellano'
    idioma = get_object_or_404(Idioma, nombre=idioma_nombre)
    libros = Libro.objects.filter(genero__nombre='Filosofía', idioma=idioma).order_by('-fecha_creacion')
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'filosofia.html', context)

def poesia(request):
    idioma_nombre = request.session.get('idioma_seleccionado', None)
    if idioma_nombre is None:
        idioma_nombre = 'Castellano'
    idioma = get_object_or_404(Idioma, nombre=idioma_nombre)
    libros = Libro.objects.filter(genero__nombre='Poesía', idioma=idioma).order_by('-fecha_creacion')
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'poesia.html', context)

def teatro(request):
    idioma_nombre = request.session.get('idioma_seleccionado', None)
    if idioma_nombre is None:
        idioma_nombre = 'Castellano'
    idioma = get_object_or_404(Idioma, nombre=idioma_nombre)
    libros = Libro.objects.filter(genero__nombre='Teatro', idioma=idioma).order_by('-fecha_creacion')
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'teatro.html', context)

def novela(request):
    idioma_nombre = request.session.get('idioma_seleccionado', None)
    if idioma_nombre is None:
        idioma_nombre = 'Castellano'
    idioma = get_object_or_404(Idioma, nombre=idioma_nombre)
    libros = Libro.objects.filter(genero__nombre='Novela', idioma=idioma).order_by('-fecha_creacion')
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'novela.html', context)

def cambiar_idioma(request):
    if request.method == 'POST':
        idioma = request.POST.get('idioma')
        if idioma:
            request.session['idioma_seleccionado'] = idioma 
    return redirect(request.META.get('HTTP_REFERER', '/'))



