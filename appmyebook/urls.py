from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('literaturaClasica/', views.literaturaClasica, name='literaturaClasica'),
    path('filosofia/', views.filosofia, name='filosofia'),
    path('poesia/', views.poesia, name='poesia'),
    path('teatro/', views.teatro, name='teatro'),
    path('novela/', views.novela, name='novela'),
    path('cambiar_idioma/', views.cambiar_idioma, name='cambiar_idioma'),
    path('libro/<int:libro_id>', views.detalle_libro, name='detalle_libro'),
    
    path('libro/<int:genero_id>/<int:idioma_id>/', views.index_libro, name='index_libro')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)