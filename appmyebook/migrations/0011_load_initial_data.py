from django.db import migrations

def add_genre(apps, schema_editor):
    Genre = apps.get_model('appmyebook', 'Genero')

    genres = [
        {"nombre": "Novela", "descripcion": "La novela es un género literario..."}
    ]

    for genre in genres:
        Genre.objects.create(
            nombre=genre["nombre"],
            descripcion=genre["descripcion"]
        )

def add_idioma(apps, schema_editor):
    Idioma = apps.get_model('appmyebook', 'Idioma')

    idiomas = [
        {"nombre": "Castellano"}
    ]

    for idioma in idiomas:
        Idioma.objects.create(
            nombre=idioma["nombre"]
        )

def add_libro(apps, schema_editor):
    Libro = apps.get_model('appmyebook', 'Libro')
    Genero = apps.get_model('appmyebook', 'Genero')
    Idioma = apps.get_model('appmyebook', 'Idioma')

    libros = [
        {"titulo": "Roma soy yo", "autor": "Santiago Posteguillo", "isbn": "841314", "descripcion": "Descripción del libro 1", "genero": 1, "idioma": [1], "aprobado": True}
    ]

    for libro in libros:
        genero_obj = Genero.objects.get(pk=libro["genero"])
        libro_obj = Libro.objects.create(
            titulo=libro["titulo"],
            autor=libro["autor"],
            isbn=libro["isbn"],
            descripcion=libro["descripcion"],
            genero=genero_obj,
            aprobado=libro["aprobado"]
        )
        for idioma_id in libro["idioma"]:
            idioma_obj = Idioma.objects.get(pk=idioma_id)
            libro_obj.idioma.add(idioma_obj)

class Migration(migrations.Migration):

    dependencies = [
        ('appmyebook', '0010_libro_aprobado'),
    ]

    operations = [
        migrations.RunPython(add_genre),
        migrations.RunPython(add_idioma),
        migrations.RunPython(add_libro),
    ]
