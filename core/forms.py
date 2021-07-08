from django import forms
from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Usuario


class UsuarioForm(forms.ModelForm):

    class Meta:
        model=Usuario
        fields = ['RutUsuario', 'image', 'NombreCom', 'Telefono', 'Direccion', 'email', 'idPais', 'password']
        labels = '__all__'


        widgets={
            'RutUsuario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su Rut',
                    'id': 'RutUsuario'
                }
            ),
             'image':forms.ClearableFileInput(
                attrs={
                    'class':'form-control',
                    'id': 'image'
                }
            ),
            'NombreCom': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre Completo',
                    'id': 'NombreCom'
                }
            ),
            'Telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Teléfono',
                    'id': 'Telefono'
                }
            ),
            'Direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Dirección',
                    'id': 'Direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Email',
                    'id': 'email'
                }
            ),
            'idPais': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Seleccione su país',
                    'id': 'pais'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Contraseña',
                    'id': 'password'
                }
            )
        }