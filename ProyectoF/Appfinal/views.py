from django.shortcuts import render
from django.http import HttpResponse, response

from Appfinal.models import FormularioVentas, FormularioCursos
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

        return render(request, "Appfinal/resultadoBusqueda.html", {"clientes": clientes, "nombre":nombre } )

    else:

        respuesta = "Che, mandame informacion"

    return HttpResponse(respuesta)

#CRUD AVANZADO

def leerClientes(request):
    clientes = FormularioVentas.objects.all()
    dir = {"clientes": clientes}
    return render(request, "Appfinal/leerClientes.html", dir)

def eliminarCliente(request, clienteQueQuieroBorrar):
    clienteQueBorro = FormularioVentas.objects.get(nombre=clienteQueQuieroBorrar)
    clienteQueBorro.delete()

    #vuelvo al menu
    clientes = FormularioVentas.objects.all()
    dir = {"clientes": clientes}
    return render(request, "Appfinal/leerClientes.html", dir)

def editarCliente(request, clienteQueQuieroEditar):
        cliente = FormularioVentas.objects.get(nombre = clienteQueQuieroEditar)
        if request.method == "POST":
            miFormulario = FormularioVentas(request.POST)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data

                cliente.nombre = informacion['nombre'],
                cliente.telefono = informacion['telefono']

                cliente.save()
                return render(request, "Appfinal/editarCliente.html")
            else:
                miFormulario = FormularioVentas(initial={"nombre": cliente.nombre, "telefono": cliente.telefono} )


        return render(request, 'Appfinal/editarCliente.html')  


def formularioCursos(request):
    if request.method == "POST":
            curso = FormularioCursos(curso=request.POST['curso'], comision= request.POST['comision'])
            curso.save()
            return render(request, "Appfinal/inicio.html")


    return render(request, 'Appfinal/formularioCursos.html')  
    



            