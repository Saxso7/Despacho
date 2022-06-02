from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_despacho, name="ventas"),
    path('put',views.put_despacho_postVentas, name="crear"),
    path('delete',views.EliminarDespachos, name="eliminar")
]