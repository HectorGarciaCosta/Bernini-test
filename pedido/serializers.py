from rest_framework import serializers
from .models import Pedido, Articulo

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo

        fields = '__all__'