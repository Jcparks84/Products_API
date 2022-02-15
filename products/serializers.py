from dataclasses import field
from rest_framework import serializers
from .models import Products

class ProductsSerializers(serializers.ModelSerializers):
    class Meta:
        model = Products
        fields = ['name', 'color', 'weight', 'price']
