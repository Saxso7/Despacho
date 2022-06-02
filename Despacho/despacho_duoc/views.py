from django.shortcuts import render
import requests 
import json

def index(request):
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

def seguimiento(request):
    return render(request, 'seguimiento.html',{

    })

