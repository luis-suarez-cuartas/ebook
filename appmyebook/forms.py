from xml.dom import ValidationErr
from django import forms
from .models import Genero, Libro
class LibroForm(forms.ModelForm):
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), empty_label="Selecciona una opción")
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'descripcion', 'genero', 'idioma', 'imagen']

    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True