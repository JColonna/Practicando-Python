from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from Appfinal.forms import UserRegisterForm
from django. contrib.auth.decorators import login_required

from Appfinal.models import FormularioVentas
from Appfinal.models import Curso 
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
@login_required
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
                return render(request, "Appfinal/formularioVentas.html")
            else:
                miFormulario = FormularioVentas(initial={"nombre": cliente.nombre, "telefono": cliente.telefono} )


        return render(request, 'Appfinal/formularioVentas.html')  
    

#CVB crud pero avanzado

class CursoList(ListView):

    model = Curso
    template_name ="Appfinal/curso_list.html"

class CursoDetail(DetailView):
    model = Curso
    template_name ="Appfinal/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "../Appfinal/curso/list"
    fields = ["curso", "comision"]

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "../curso/list"
    fields = ["curso", "comision"]


class CursoDelete(DeleteView):
    model = Curso
    success_url = "../curso/list"





def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request, "Appfinal/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "Appfinal/inicio.html", {"mensaje": "Los datos ingresados no son validos, vuelve a intenarlo"})


        else:
            return render(request, "Appfinal/inicio.html", {"mensaje": "Formulario erroneo"})
            
    form = AuthenticationForm() #Formulario vacio para hacer el login
    return render(request, "Appfinal/login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"Appfinal/inicio.html", {"mensaje": f"{username} Creado"})
    
    
    
    else:
        form = UserRegisterForm()
    return render(request, "Appfinal/register.html", {"form": form})


@login_required  
def editarPerfil(request):

   usuario= request.user

   if request.method == "POST":

      miFormulario= UserEditForm(request.POST)  

      if miFormulario.is_valid():

         informacion= miFormulario.cleaned_data

         usuario.email= informacion["email"] 
         usuario.password1= informacion["password1"]
         usuario.password2= informacion["password2"]
         usuario.last_name= informacion["last_name"]
         usuario.first_name= informacion["first_name"]

         usuario.save()

         return render(request, "Appfinal/inicio.html")

   else:
      miFormulario= UserEditForm(initial={"email":usuario.email})  

   return render (request, "Appfinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario}) 




            