from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label = "Nombre:")
    email = forms.EmailField(label = "Email")
    consulta = forms.CharField(label = "Mensaje")
    

