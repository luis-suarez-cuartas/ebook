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
    consulta = '''SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY genero_id ORDER BY fecha_creacion DESC) as rn FROM appmyebook_libro) as subquery WHERE rn = 1'''
    ultimos_libros = Libro.objects.raw(consulta)
    context = {'ultimos_libros': ultimos_libros}
    return render(request, 'index.html', context)

# Vista para mostrar los libros de un género específico
def show_genero(request, genero_id):
    genero = get_object_or_404(Genero, pk=genero_id)
    libros = genero.libro_set.all().order_by('-fecha_creacion')
    context = {'libros': libros, 'genero': genero}
    return render(request, 'show_genero.html', context)

# Vista para mostrar los libros en un idioma específico
def show_idioma(request, idioma_id):
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = Libro.objects.filter(idioma=idioma).order_by('-fecha_creacion') # La vista show_idioma, el modelo Libro tiene una relación ManyToManyField con Idioma, lo que significa que idioma.libro_set no estará disponible directamente. Django no crea related managers automáticamente para ManyToManyField. En este caso, necesitamos usar la consulta normal.
    context = {'libros': libros, 'idioma': idioma}
    return render(request, 'show_idioma.html', context)

def cambiar_idioma(request):
    if request.method == 'POST':
        idioma = request.POST.get('idioma')
        if idioma:
            request.session['idioma_seleccionado'] = idioma 
    return redirect(request.META.get('HTTP_REFERER', '/'))

def show_libro(request):
    libros = Libro.objects.all().order_by('-fecha_creacion')
    context = {'libros': libros}
    return render(request, 'show_libro.html', context)




