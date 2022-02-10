from django.shortcuts import render, redirect, HttpResponse
from .logica import Articulo
from .consultasORM import listaIdClientes, consultaClientes
import random

# Create your views here.




def vistaInicio(request):
    
    #Suponemos que nuestra vista inicio, también devuelve alguos artículos de inicio.
    
    listaArticulos = []
    listaArticulos.append(Articulo("En psp estamos dando django","En el segundo trimestre estamos dando django"))
    listaArticulos.append(Articulo("Nuevas practicas en Redes grado medio","Se han comprado rar y paneles de parcheo para las prácticas"))
    contexto = {
        "listaArticulos" : listaArticulos, 
    }
    return render(request, "index.html",contexto)
    


def vistaClientes(request):
    
    
    #Suponemos que nuestra vista Clientes, también devuelve algunos clientes.
    return render(request, "clientes.html",{})

#Os recuerdo que a la vistaContacto, se puede acceder de dos métodos.....
def vistaContacto(request):
    #Suponemos que nuestra vista Contacto, manda un formulario.
    #return render(request, "contacto.html",{})
    
    if (request.method =="GET"):
        print ("Método get")
        return render(request, "contacto.html", {})
    else:
        print ("Método POST")
        #otro ejemplo con redirect
        return redirect('Inicio')


def vistaAcercade(request):
    return render(request, "acercade.html",{})


def inicioClientes(request):
    listaClientes = listaIdClientes();  #lista de clientes
    id1 = random.choice(listaClientes)
    listaClientes.remove(id1)
    
    id2 = random.choice(listaClientes)
    listaClientes.remove(id2)
    
    id3 = random.choice(listaClientes)
    listaClientes.remove(id3)
    
    listaClientes = [consultaClientes(id1), consultaClientes(id2), consultaClientes(id3)]
    print (listaClientes)
    
    contexto = {
        'lista' : listaClientes
    }
    return render(request, 'clientes.html', contexto)
    
    
