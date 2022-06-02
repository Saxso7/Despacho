from rest_framework import serializers
from .models import Despacho, Post_ventas


class DespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despacho
        fields = '__all__'

class PostVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_ventas
        fields = '__all__'