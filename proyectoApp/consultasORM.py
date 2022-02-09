from .models import *

def listaIdArticulo():
    misArticulos = Articulo.objects.filter(
        estado = True,
        publicado = True
    
    ).values_list('id', flat = True)
    
    listaArticulos = list(misArticulos)
    return listaArticulos


def consultaArticulo(id1):
    return Articulo.objects.get(id = id1)




def listaIdCliente():
    misClientes = Cliente.objects.filter(
        estado = True,
        publicado = True
    
    ).values_list('id', flat = True)
    
    listaClientes = list(misClientes)
    return listaClientes


def consultaClientes(id1):
    return Cliente.objects.get(id = id1)