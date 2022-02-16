from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductsSerializer
from .models import Products


@api_view(['GET'])
def products_list(request):

    products = Products.objects.all()

    serializer = ProductsSerializer(products, many = True)



    return Response(serializer.data)

