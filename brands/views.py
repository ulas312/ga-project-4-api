from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Brand
from .serializers.common import BrandSerializer


class BrandListView(APIView):

    def get(self, _request):
        brands = Brand.objects.all()  
        serialized_products = BrandSerializer(brands, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)