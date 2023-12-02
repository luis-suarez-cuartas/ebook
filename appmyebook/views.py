from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.db.models import Max
from .models import Libro, Genero, Idioma
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import LibroForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consulta = '''
            SELECT * FROM (
                SELECT *, ROW_NUMBER() OVER (PARTITION BY genero_id ORDER BY fecha_creacion DESC) as rn 
                FROM appmyebook_libro
            ) as subquery WHERE rn = 1
        '''
        ultimos_libros = Libro.objects.raw(consulta)
        context['ultimos_libros'] = ultimos_libros
        return context
    
class ShowLibroView(ListView):
    model = Libro
    template_name = 'show_libro.html'  
    context_object_name = 'libros'     

    def get_queryset(self):
        return Libro.objects.all().order_by('-fecha_creacion')  


class ShowGeneroView(ListView):
    model = Libro
    template_name = 'show_genero.html'
    context_object_name = 'libros'

    def get_queryset(self):
        genero_id = self.kwargs['genero_id']
        genero = get_object_or_404(Genero, pk=genero_id)
        return genero.libro_set.all().order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genero_id = self.kwargs['genero_id']
        context['genero'] = get_object_or_404(Genero, pk=genero_id)
        return context

class ShowIdiomaView(ListView):
    model = Libro
    template_name = 'show_idioma.html'
    context_object_name = 'libros'

    def get_queryset(self):
        idioma_id = self.kwargs['idioma_id']
        idioma = get_object_or_404(Idioma, pk=idioma_id)
        return Libro.objects.filter(idioma=idioma).order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idioma_id = self.kwargs['idioma_id']
        context['idioma'] = get_object_or_404(Idioma, pk=idioma_id)
        return context
    
class DetalleLibroView(DetailView):
    model = Libro
    template_name = 'detalle_libro.html'
    context_object_name = 'libro'

    def get_object(self, queryset=None):
        libro_id = self.kwargs['libro_id']
        return get_object_or_404(Libro, pk=libro_id)
    
class AgregarLibroView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'agregarLibros.html'

def cambiar_idioma(request):
    if request.method == 'POST':
        idioma = request.POST.get('idioma')
        if idioma:
            request.session['idioma_seleccionado'] = idioma 
    return redirect(request.META.get('HTTP_REFERER', '/'))




# devuelve los libros de un genero y un idioma
def index_libro(request, genero_id, idioma_id):
    genero = get_object_or_404(Genero, pk=genero_id)
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = get_list_or_404(Libro, genero=genero, idioma=idioma)
    context = {'libros': libros}
    return render(request, 'generoIdioma.html', context) #TODO generoIdioma.html no existe



