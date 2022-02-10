from .models import *

def listaIdArticulos():
    misArticulos = Articulo.objects.filter(
        estado = True
        
    
    ).values_list('id', flat = True)
    
    listaArticulos = list(misArticulos)
    return listaArticulos


def consultaArticulos(id1):
    return Articulo.objects.get(id = id1)




def listaIdClientes():
    misClientes = Cliente.objects.filter(
        estado = True
        
    
    ).values_list('id', flat = True)
    
    listaClientes = list(misClientes)
    return listaClientes


def consultaClientes(id1):
    return Cliente.objects.get(id = id1)