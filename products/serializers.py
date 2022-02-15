from dataclasses import field
from rest_framework import serializer
from .models import Products

class ProductsSerializer(serializer.ModelSerializers):
    class Meta:
        model = Products
        fields = ['name', 'color', 'weight', 'price']
