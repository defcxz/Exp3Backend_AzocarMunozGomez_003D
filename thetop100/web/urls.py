from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('nosotros', views.nosotros, name="nosotros"),
   path('galeria', views.galeria, name="galeria"),
   path('registro', views.registro, name="registro"),
   path('contacto', views.contacto, name="contacto"),
]