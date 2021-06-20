from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

# Create your views here.

def home(request):
   return render(request, 'home.html')

def galeria(request):
   return render(request, 'galeria.html')

def contacto(request):
   
   return render(request, 'contacto.html')


def crearMensaje(request):
   if request.method == 'POST':
      mensaje_form = MensajeForm(request.POST)
      if mensaje_form.is_valid():
         mensaje_form.save()
         return redirect('contacto')
   else:
      mensaje_form = MensajeForm()
   return render(request, 'contacto.html',{'mensaje_form':mensaje_form})

def Ver(request):
   mensajes = Mensaje.objects.all()

   return render(request, 'ver.html', context={'datos':mensajes})

def form_modMensaje(request,id):
   men= Mensaje.objects.get(id=id)
   
   datos ={
      'form': MensajeForm(instance=men)
   }
   if request.method == 'POST':
      formulario= MensajeForm(data=request.POST, instance = men)
      if formulario.is_valid:
         formulario.save()
         return redirect('ver')
   return render(request, 'form_modMensaje.html', datos)

def form_delMensaje(request, id):
   men= Mensaje.objects.get(id=id)
   men.delete()
   return redirect('ver')
