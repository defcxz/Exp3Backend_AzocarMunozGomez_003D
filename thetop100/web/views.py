from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'home.html')

def nosotros(request):
   return render(request, 'nosotros.html')

def galeria(request):
   return render(request, 'galeria.html')

def registro(request):
   return render(request, 'Registro.html')

def contacto(request):
   return render(request, 'contacto.html')