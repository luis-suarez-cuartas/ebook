from .models import Genero, Idioma

def generos_context(request):
    generos = Genero.objects.all()
    return {'generos': generos}