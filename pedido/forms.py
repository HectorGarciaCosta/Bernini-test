from django import forms
from .models import Pedido, Articulo

class PostForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ('numero',)

class PostFormArticulos(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ('GLN','precio',)
