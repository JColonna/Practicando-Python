from django.urls import path
from Appfinal import views
from Appfinal.views import CursoList, CursoDetail
from django.contrib.auth.views import LogoutView

from Appfinal.views import editarPerfil


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

    #CVB
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetail.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Update'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    
    #Login, registro y logout
    
    path('login', views.login_request, name='Login'),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name="Appfinal/logout.html"), name="Logout"),
    path('editarperfil', views.editarPerfil, name="EditarPerfil")

]