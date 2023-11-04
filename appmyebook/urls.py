from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filosofia/', views.filosofia, name='filosofia'),
    path('literaturaClasica/', views.literaturaClasica, name='literaturaClasica'),
    path('novela/', views.novela, name='novela'),
    path('poesia/', views.poesia, name='poesia'),
    path('teatro/', views.teatro, name='teatro'),
    path('libro/<int:libro_id>', views.show_libro, name='show_libro'),
    path('libro/<int:genero_id>/<int:idioma_id>/', views.index_libro, name='index_libro')
]