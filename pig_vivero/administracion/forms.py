from django import forms
from django.forms import ValidationError
from administracion.models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    """ Este es el formulario asociado al modelo producto """
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.FloatField(label='Precio', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(label='Cantidad', widget=forms.TextInput(attrs={'class': 'form-control'}))
    imagen = forms.FileInput(attrs={'class':'form-control'})
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
         label='Categoria', widget=forms.Select(attrs={'class': 'form-control'}))
    promocion = forms.BooleanField(label='Promocionar', widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    

    class Meta: 
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'imagen', 'categoria', 'promocion']


class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre' , max_length=250, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
         model = Categoria
         fields = ['nombre']