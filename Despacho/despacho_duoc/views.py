from django.shortcuts import render

def index(request):
    return render(request, 'index.html',{
        'Seguimiento': 'Seguimiento',
        'Pagina' : 'Todo suyo el proyecto cauros'
    })
