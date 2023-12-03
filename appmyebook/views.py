from urllib.parse import urljoin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.db.models import Max
from django.urls import reverse_lazy

from ebook import settings
from .models import Libro, Genero, Idioma
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import LibroForm

from django.utils.translation import gettext as _, gettext_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consulta = '''
            SELECT * FROM (
                SELECT *, ROW_NUMBER() OVER (PARTITION BY genero_id ORDER BY fecha_creacion DESC) as rn 
                FROM appmyebook_libro WHERE aprobado = True
            ) as subquery WHERE rn = 1
        '''
        context['ultimos_libros'] = Libro.objects.raw(consulta)
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return self.handle_ajax_request()
        else:
            return super().get(request, *args, **kwargs)

    def handle_ajax_request(self):
        ultimos_libros = Libro.objects.raw('''
            SELECT * FROM (
                SELECT *, ROW_NUMBER() OVER (PARTITION BY genero_id ORDER BY fecha_creacion DESC) as rn 
                FROM appmyebook_libro WHERE aprobado = True
            ) as subquery WHERE rn = 1
        ''')
        data = [{
            'id': libro.id,
            'titulo': libro.titulo,
            'imagen_url': libro.imagen.url if libro.imagen else settings.MEDIA_URL + "default.jpg"
        } for libro in ultimos_libros]
        return JsonResponse({'ultimos_libros': data})
    
class ShowLibroView(ListView):
    model = Libro
    template_name = 'show_libro.html'
    context_object_name = 'libros'

    def get_queryset(self):
        return Libro.objects.filter(aprobado=True).order_by('-fecha_creacion')

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            libros = self.get_queryset().values('id', 'titulo', 'imagen')
            for libro in libros:
                if libro['imagen']:
                    libro['imagen_url'] = self.request.build_absolute_uri(settings.MEDIA_URL + libro['imagen'])
                else:
                    libro['imagen_url'] = settings.MEDIA_URL + "default.jpg"
            return JsonResponse(list(libros), safe=False)
        else:
            return super().render_to_response(context, **response_kwargs)

class ShowGeneroView(ListView):
    model = Libro
    template_name = 'show_genero.html'
    context_object_name = 'libros'

    def get_queryset(self):
        genero_id = self.kwargs['genero_id']
        genero = get_object_or_404(Genero, pk=genero_id)
        return genero.libro_set.filter(aprobado=True).order_by('-fecha_creacion')
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            libros = list(self.get_queryset().values('id', 'titulo', 'imagen'))
            for libro in libros:
                if libro['imagen']:
                    libro['imagen_url'] = self.request.build_absolute_uri(settings.MEDIA_URL + libro['imagen'])
                else:
                    libro['imagen_url'] = settings.MEDIA_URL + "default.jpg"
            genero_data = {
                'nombre': self.object_list[0].genero.nombre,
                'descripcion': self.object_list[0].genero.descripcion
            }
            data = {
                'libros': libros,
                'genero': genero_data
            }
            return JsonResponse(data)
        else:
            return super().render_to_response(context, **response_kwargs)

class ShowIdiomaView(ListView):
    model = Libro
    template_name = 'show_idioma.html'
    context_object_name = 'libros'

    def get_queryset(self):
        idioma_id = self.kwargs['idioma_id']
        idioma = get_object_or_404(Idioma, pk=idioma_id)
        return Libro.objects.filter(idioma=idioma, aprobado=True).order_by('-fecha_creacion')

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            idioma_id = self.kwargs['idioma_id']
            idioma = get_object_or_404(Idioma, pk=idioma_id)
            libros = list(self.get_queryset().values('id', 'titulo', 'imagen'))
            for libro in libros:
                if libro['imagen']:
                    libro['imagen_url'] = self.request.build_absolute_uri(settings.MEDIA_URL + libro['imagen'])
                else:
                    libro['imagen_url'] = settings.MEDIA_URL + "default.jpg"
            idioma_data = {
                'nombre': idioma.nombre
            }
            data = {
                'libros': libros,
                'idioma': idioma_data
            }
            return JsonResponse(data)
        else:
            return super().render_to_response(context, **response_kwargs)

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
    def get_success_url(self):
        return reverse_lazy('index')

def cambiar_idioma(request):
    if request.method == 'POST':
        idioma = request.POST.get('idioma')
        if idioma:
            request.session['idioma_seleccionado'] = idioma
    return redirect(request.META.get('HTTP_REFERER', '/'))

def index_libro(request, genero_id, idioma_id):
    genero = get_object_or_404(Genero, pk=genero_id)
    idioma = get_object_or_404(Idioma, pk=idioma_id)
    libros = get_list_or_404(Libro, genero=genero, idioma=idioma, aprobado=True)
    context = {'libros': libros}
    return render(request, 'generoIdioma.html', context)


