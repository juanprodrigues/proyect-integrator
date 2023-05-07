from django import forms
from django.core.exceptions import ValidationError

# Formulario de contacto
class Contacto(forms.Form):
    nombre = forms.CharField(label="Nombre ",widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    apellido = forms.CharField(label="Apellido ",widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    mail = forms.EmailField(label="Correo",widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    telefono = forms.IntegerField(label="Telefono ",widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    mensaje = forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)


    def clean_mensaje(self):
    # Validación del campo Mail
        data = self.cleaned_data["mensaje"]
        print("sg",data)
        #TODO: Validar que el correo no tenga consultas repetidas
        if True:
            raise ValidationError('El campo de nombre no puede estar vacío')
        
        return data

    def clean(self):
        pass