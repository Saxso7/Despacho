from distutils.command.config import config
from django.shortcuts import render
import pyrebase
import requests 
import json


config={
    "apiKey": "AIzaSyAE-OQSu-G2-GE9o7t_D7buR-4DPXkOGH8",
    "authDomain": "django-df2d3.firebaseapp.com",
    "databaseURL": "https://django-df2d3-default-rtdb.firebaseio.com",
    "projectId": "django-df2d3",    
    "storageBucket": "django-df2d3.appspot.com",
    "messagingSenderId": "360877144688",
    "appId": "1:360877144688:web:f0377c7f646a80004492b5",
   
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

"""def index(request):
    url = 'https://claudiorigollet.cl/api/products/'
    response = requests.get(url)
    if response.status_code == 200:
        response_json = json.loads(response.content)
        print(response_json)
        return render(request, 'index.html', {
        'response_json': response_json['products'],
        'despacho': 'Pagina de despacho'
        })
    
    print(response.content)
"""
def seguimiento(request):
    return render(request, 'seguimiento.html',{

    })

def misCompras(request):
    return render(request, 'misCompras.html',{

    })
    

    
def index(request):

    channel_direccion = database.child('data').child('direccion').get().val()
    channel_nombre = database.child('data').child('nombre').get().val()
    channel_rut = database.child('data').child('rut').get().val()
    channel_telefono = database.child('data').child('telefono').get().val()
    channel_producto = database.child('data').child('producto').get().val()
    channel_precio = database.child('data').child('precio').get().val()
    channel_distancia = database.child('data').child('distancia').get().val()
    
    channel_direccion2 = database.child('data').child('direccion2').get().val()

    channel_nombre2 = database.child('data').child('nombre2').get().val()
    channel_rut2 = database.child('data').child('rut2').get().val()
    channel_telefono2 = database.child('data').child('telefono2').get().val()
    channel_producto2 = database.child('data').child('producto2').get().val()
    channel_precio2 = database.child('data').child('precio2').get().val()
    channel_distancia2 = database.child('data').child('distancia2').get().val()
    

    channel_direccion3 = database.child('data').child('direccion3').get().val()
    channel_nombre3 = database.child('data').child('nombre').get().val()
    channel_rut3 = database.child('data').child('rut3').get().val()
    channel_telefono3 = database.child('data').child('telefono3').get().val()
    channel_producto3 = database.child('data').child('producto').get().val()
    channel_precio3 = database.child('data').child('precio3').get().val()
    channel_distancia3 = database.child('data').child('distancia').get().val()

    channel_direccion4 = database.child('data').child('direccion4').get().val()
    channel_nombre4 = database.child('data').child('nombre4').get().val()
    channel_rut4 = database.child('data').child('rut4').get().val()
    channel_telefono4 = database.child('data').child('telefono4').get().val()
    channel_producto4 = database.child('data').child('producto').get().val()
    channel_precio4 = database.child('data').child('precio4').get().val()
    channel_distancia4 = database.child('data').child('distancia4').get().val()

    channel_direccion5 = database.child('data').child('direccion5').get().val()
    channel_nombre5 = database.child('data').child('nombre5').get().val()
    channel_rut5 = database.child('data').child('rut5').get().val()
    channel_telefono5 = database.child('data').child('telefono5').get().val()
    channel_producto5 = database.child('data').child('producto5').get().val()
    channel_precio5 = database.child('data').child('precio5').get().val()
    channel_distancia5 = database.child('data').child('distancia5').get().val()
    
    return render (request, 'index.html',{
        "channel_direccion":channel_direccion,
        "channel_nombre":channel_nombre,
        "channel_rut":channel_rut,
        "channel_telefono":channel_telefono,
        "channel_producto":channel_producto,
        "channel_precio":channel_precio,
        "channel_distancia":channel_distancia,

        "channel_direccion2":channel_direccion2,
        "channel_nombre2":channel_nombre2,
        "channel_rut2":channel_rut2,
        "channel_telefono2":channel_telefono2,
        "channel_producto2":channel_producto2,
        "channel_precio2":channel_precio2,
        "channel_distancia2":channel_distancia2,

        "channel_direccion3":channel_direccion3,
        "channel_nombre3":channel_nombre3,
        "channel_rut3":channel_rut3,
        "channel_telefono3":channel_telefono3,
        "channel_producto3":channel_producto3,
        "channel_precio3":channel_precio3,
        "channel_distancia3":channel_distancia3,

        "channel_direccion4":channel_direccion4,
        "channel_nombre4":channel_nombre4,
        "channel_rut4":channel_rut4,
        "channel_telefono4":channel_telefono4,
        "channel_producto4":channel_producto4,
        "channel_precio4":channel_precio4,
        "channel_distancia4":channel_distancia4,

        "channel_direccion5":channel_direccion5,
        "channel_nombre5":channel_nombre5,
        "channel_rut5":channel_rut5,
        "channel_telefono5":channel_telefono5,
        "channel_producto5":channel_producto5,
        "channel_precio5":channel_precio5,
        "channel_distancia5":channel_distancia5 
   
})
