from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

# Create your views here.

def home(request):
   return render(request, 'home.html')

def galeria(request):
   return render(request, 'galeria.html')

def contacto(request):
   
   mensajes = Mensaje.objects.all()
   return render(request, 'contacto.html', context={'datos': mensajes}
   )


def crearMensaje(request):
   if request.method == 'POST':
      mensaje_form = MensajeForm(request.POST)
      if mensaje_form.is_valid():
         mensaje_form.save()
         return redirect('contacto')
   else:
      mensaje_form = MensajeForm()
   return render(request, 'contacto.html',{'mensaje_form':mensaje_form})