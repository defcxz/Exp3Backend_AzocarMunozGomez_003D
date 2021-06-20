from django.urls import path
from .views import home, galeria, contacto, crearMensaje, Ver, form_modMensaje, form_delMensaje

urlpatterns = [
   path('', home, name="home"),
   path('galeria', galeria, name="galeria"),
   path('contacto', contacto, name="contacto"),
   path('crear_mensaje', crearMensaje, name="crearMensaje"),
   path('ver', Ver, name="ver"),
   path('form_modMensaje/<id>', form_modMensaje, name="form_modMensaje"),
   path('form_delMensaje/<id>', form_delMensaje, name="form_delMensaje")
]