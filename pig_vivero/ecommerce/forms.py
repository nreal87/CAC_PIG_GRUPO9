from django import forms
from django.forms import ValidationError
from ecommerce.models import Producto, Categoria

def validar_nombre(nombre):

    for caracter in nombre:
        if not caracter.isalpha():
            raise ValidationError('ERROR. El nombre solo debe tener letras.',
                                  code='Error',
                                  params={'nombre': nombre})


class ContactoForm(forms.Form):
    SUCURSALES = (('', 'Seleccione Sucursal'),
                  ('1', 'Córdoba'),
                  ('2', 'Buenos Aires'),
                  ('3', 'Mendoza'),
                  ('4', 'Rosario'),
                  ('5', 'CABA') )
    
    nombre = forms.CharField(label="Nombre",
                             max_length=50,
                             required=True,
                             validators=(validar_nombre,)
                             )    
    
    email = forms.EmailField(label="Email", max_length=70,
                             widget=forms.TextInput(attrs={'placeholder': 'ejemplo@dominio.com',}),
                             required=True)
    
    sucursal = forms.ChoiceField(
        label='Sucursal',
        choices=SUCURSALES,
        widget=forms.Select(attrs={'id': 'sucursal'}),
        required=False
        )
     
    consulta = forms.CharField(label = "Mensaje",
                               max_length=250,
                               widget=forms.Textarea(attrs={'placeholder': 'Ingrese su consulta.'}),
                               required=True)

    def clean_consulta(self):
        data = self.cleaned_data['consulta']
        if len(data) < 10:
            raise ValidationError("La consulta ingresada es muy corta.",
                                   code='Error')
        return self.cleaned_data['consulta']

class ProductoForm(forms.ModelForm):
    codigo = forms.CharField(label='Código', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(label='Descripcion', widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.FloatField(label='Precio', widget=forms.TextInput(attrs={'class': 'form-control'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
         label='Categoria', widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta: 
        model = Producto
        fields = ['codigo', 'nombre', 'descripcion', 'precio', 'categoria']