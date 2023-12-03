from xml.dom import ValidationErr
from django import forms
from .models import Genero, Libro
from django.utils.translation import gettext_lazy as _

class LibroForm(forms.ModelForm):
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), empty_label=_("Selecciona una opción"))
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'isbn', 'descripcion', 'genero', 'idioma', 'imagen']

    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True