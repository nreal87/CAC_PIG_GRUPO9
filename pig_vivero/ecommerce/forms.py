from django import forms
from django.forms import ValidationError

def validar_nombre(nombre):

    for caracter in nombre:
        if not caracter.isalpha():
            raise ValidationError('ERROR. El nombre solo debe tener letras.',
                                code='Error',
                                params={'nombre': nombre})


class ContactoForm(forms.Form):

    nombre = forms.CharField(label="Nombre",
                             max_length=50,
                             required=True,
                             validators=(validar_nombre,)
                             )    
    
    email = forms.EmailField(label="Email", max_length=70,
                             widget=forms.TextInput(attrs={'placeholder': 'ejemplo@dominio.com'}),
                             required=True)
    
    provincia = forms.ChoiceField(
                            label='Provincia',
                            widget=forms.Select(attrs={'id': 'provincia'}),
                            required=False)
    
    consulta = forms.CharField(label = "Mensaje",
                               max_length=250,
                               widget=forms.Textarea(attrs={'placeholder': 'Ingrese su consulta.'}),
                               required=True)

    def clean_consulta(self):
        data = self.cleaned_data['consulta']
        if len(data) < 10:
            raise ValidationError("La consulta ingresada es muy corta.",
                                   code='Error')
        return data

