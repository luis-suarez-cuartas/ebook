from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ShowGeneroView
from .views import ShowIdiomaView
from .views import DetalleLibroView
from .views import ShowLibroView
from .views import IndexView
from .views import AgregarLibroView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('genero/<int:genero_id>/', ShowGeneroView.as_view(), name='show_genero'),
    path('idioma/<int:idioma_id>/', ShowIdiomaView.as_view(), name='show_idioma'),
    path('libros/', ShowLibroView.as_view(), name='show_libro'),
    path('libro/<int:libro_id>/', DetalleLibroView.as_view(), name='detalle_libro'),
    path('cambiar_idioma/', views.cambiar_idioma, name='cambiar_idioma'),
    path('libro/<int:genero_id>/<int:idioma_id>/', views.index_libro, name='index_libro'),
    path('libro/agregar/', AgregarLibroView.as_view(), name='agregarLibros'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
