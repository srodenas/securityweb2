from django.urls import path
from proyectoApp.views import vistaInicio, vistaClientes, vistaAcercade, vistaContacto, inicioClientes


urlpatterns = [
    path('', vistaInicio),
    path('inicio/', vistaInicio, name="Inicio"),
    path('clientes/', vistaClientes, name="Clientes"),
    path('contacto/', vistaContacto, name="Contacto"),
    path('acerca/', vistaAcercade, name="Acerca_de"),
    path('clientesOrm/', inicioClientes, name="Clientesorm"),
]
