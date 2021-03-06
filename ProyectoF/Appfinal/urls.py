from django.urls import path
from Appfinal import views


urlpatterns = [
   
    path('contacto', views.contacto, name = "Contacto"),
    path('inicio', views.inicio, name="Inicio"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('ventas', views.ventas, name='Ventas'),
    path('formularioventas', views.formularioVentas, name='FormularioVentas'),
    path('busquedaclientes', views.busquedaClientes, name='BusquedaClientes'),
    path('buscar/', views.buscar, name='Buscar'),
    path('leerclientes', views.leerClientes, name='LeerClientes'),
    path('eliminarcliente/<clienteQueQuieroBorrar>', views.eliminarCliente, name='EliminarCliente'),
    path('editarcliente/<clienteQueQuieroEditar>', views.editarCliente, name='EditarCliente'),
    path('formulariocursos', views.formularioCursos, name='FormularioCursos')


]