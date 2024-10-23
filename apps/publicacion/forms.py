from .models import Categoria, Publicacion
from django import forms


class PublicacionForm(forms.ModelForm):
    nueva_categoria = forms.CharField(required=False, label="Nueva Categoría")

    class Meta:
        model = Publicacion
        fields = ['titulo_publicacion', 'publicacion', 'categoria', 'imagen']

    def __init__(self, *args, **kwargs):
        super(PublicacionForm, self).__init__(*args, **kwargs)
        self.fields['titulo_publicacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['publicacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['imagen'].widget = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control'})
        self.fields['nueva_categoria'].widget.attrs.update({'class': 'form-control'})


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de la categoría'})
