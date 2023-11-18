from django import forms
from django.forms import ValidationError
from administracion.models import Producto, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    """ Formulario asociado al modelo producto """
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.FloatField(label='Precio', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(label='Cantidad', widget=forms.TextInput(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    categoria = forms.ModelChoiceField (queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    promocion = forms.BooleanField(widget=forms.CheckboxInput(), label='Promocionar', required=False)
    
    class Meta: 
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'imagen', 'categoria', 'promocion']


class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre' , max_length=250, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
         model = Categoria
         fields = ['nombre']


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']