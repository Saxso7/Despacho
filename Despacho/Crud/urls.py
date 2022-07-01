from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_despacho, name="crear"),
    path('actualizar_postventa',views.put_despacho_postVentas, name="actualizarPost"),
    path('eliminar/<str:pk>/',views.EliminarDespachos, name="eliminar"),
    path('crear',views.CrearDespacho, name='crear'),
    path('crear_postventa',views.get_postVenta, name='crearPost'),
    path('crear_costo',views.get_costo, name='crearPost'),
    path('post_costo',views.CrearCosto, name='postCosto')
    
]