from django.shortcuts import render
from django.http import HttpResponse

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