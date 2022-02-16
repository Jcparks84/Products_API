from webbrowser import get
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductsSerializer
from .models import Products
from products import serializers


@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET', 'PUT','DELETE'])
def products_detail(request, pk):
    products = get_object_or_404(Products, pk=pk)
    if request.method == 'GET':
        serializer = ProductsSerializer(products)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ProductsSerializer(products, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

