from .models import Genero, Idioma

def general_context(request):
    generos = Genero.objects.all()
    idiomas = Idioma.objects.all()
    return {'generos': generos, 'idiomas': idiomas}