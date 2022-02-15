from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductsSerializer
from .models import Product


@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()

    serializer = ProductsSerializer(products, many = True)



    return Response(serializer.data)

