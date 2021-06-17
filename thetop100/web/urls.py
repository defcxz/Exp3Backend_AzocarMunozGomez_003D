from django.urls import path
from .views import home, galeria, contacto, crearMensaje

urlpatterns = [
   path('', home, name="home"),
   path('galeria', galeria, name="galeria"),
   path('contacto', contacto, name="contacto"),
   path('crear_mensaje', crearMensaje, name="crearMensaje"),
]