from django.shortcuts import render
from django.http import HttpResponse, response

from Appfinal.models import FormularioVentas
from .forms import *


# Create your views here.
def contacto(request):
    return render(request, 'Appfinal/contacto.html')

def padre(request):
    

    return render(request, 'Appfinal/padre.html') #Relaciono con el template

def inicio(request):
    return render(request, 'Appfinal/inicio.html')

def nosotros(request):
    return render(request, 'Appfinal/nosotros.html')

def ventas(request):
    return render(request, 'Appfinal/ventas.html')    

def formularioVentas(request):
    if request.method == "POST":
            cliente = FormularioVentas(nombre=request.POST['nombre'], telefono= request.POST['telefono'])
            cliente.save()
            return render(request, "Appfinal/inicio.html")


    return render(request, 'Appfinal/formularioVentas.html')  

def busquedaClientes(request):

    return render(request, 'Appfinal/busquedaClientes.html')  

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = FormularioVentas.objects.filter(nombre__icontains=nombre)
        respuesta = f'Estoy buscando el cliente que se llama: {request.GET["nombre"]} '

        return render(request, "Appfinal/resultadoBusqueda.html", {"cliente": clientes, "nombre":nombre } )

    else:

        respuesta = "Che, mandame informacion"

    return HttpResponse(respuesta)
    



            