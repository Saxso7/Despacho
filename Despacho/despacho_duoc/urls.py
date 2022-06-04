from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name= 'index.html'),
    path('seguimiento.html',views.seguimiento, name='seguimiento.html'),
    path('misCompras.html',views.misCompras, name='misCompras.html'),
    path('index.html',views.index, name= 'index.html')
]
