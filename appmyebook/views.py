from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.db.models import Max
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
    # Obtener el último libro de cada género
    """     generos = Genero.objects.all()
    ultimos_libros = []
    for genero in generos:
        ultimo_libro = Libro.objects.filter(genero=genero).order_by('-fecha_creacion').first()
        if ultimo_libro:
            ultimos_libros.append(ultimo_libro)        
    context = {'ultimos_libros': ultimos_libros}  
    return render(request, 'index.html', context) """
    context = {}
    return render(request, 'index.html', context)

# Vista para mostrar los libros de un género específico
def show_genero(request, genero_id):
    genero = get_object_or_404(Genero, pk=genero_id)
    libros = Libro.objects.filter(genero=genero).order_by('-fecha_creacion')
    context = {'libros': libros, 'genero': genero}
    return render(request, 'show_genero.html', context)

# Vista para mostrar los libros en un idioma específico
def show_idioma(request, idioma_id):
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = Libro.objects.filter(idioma=idioma).order_by('-fecha_creacion')
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'show_idioma.html', context)

def cambiar_idioma(request):
    if request.method == 'POST':
        idioma = request.POST.get('idioma')
        if idioma:
            request.session['idioma_seleccionado'] = idioma 
    return redirect(request.META.get('HTTP_REFERER', '/'))



