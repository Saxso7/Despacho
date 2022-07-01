from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Despacho, Post_ventas, Costo
from .serializers import DespachoSerializer, PostVentasSerializer, CostoSerializer




@api_view(['GET'])
def get_despacho(request):
    despacho = Despacho.objects.all()
    serializer = DespachoSerializer(despacho, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_costo(request):
    costo = Costo.objects.all()
    serializer = CostoSerializer(costo, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def get_postVenta(request):
    post_venta = Post_ventas.objects.all()
    serializer = PostVentasSerializer(post_venta, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def put_despacho_postVentas(request):
    serializer = PostVentasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['DELETE'])
def EliminarDespachos(request, pk):
    despacho = Despacho.objects.get(id=pk)
    despacho.delete()

    return Response('Eliminado')

@api_view(['POST'])
def CrearDespacho(request):
    serializer = DespachoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['POST'])
def CrearCosto(request):
    serializer = CostoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


