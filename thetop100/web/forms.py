from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Mensaje

class MensajeForm(forms.ModelForm):

   class Meta:
      model = Mensaje
      fields = ['nomApellido','email','telefono','asunto','mensaje']

      labels ={
         'nomApellido': 'Nombre y Apellido',
         'email': 'Correo Electrónico',
         'telefono': 'Teléfono',
         'asunto': 'Asunto',
         'mensaje': 'Mensaje',
      }

      widgets =  {
         'nomApellido': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Ingrese nombre y apellido',
               'id':'nomapellido'
            }
         ),
         'email': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'usuario@dominio.com',
               'id':'email'
            }
         ),
         'telefono': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': '+56 9 xxxx xxxx',
               'id':'telefono'
            }
         ),
         'asunto': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Ingrese el asunto de su mensaje',
               'id':'asunto'
            }
         ),
         'mensaje': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Ingrese el mensaje',
               'id':'mensaje'
            }
         ),
      }