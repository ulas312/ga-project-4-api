from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import IntegrityError

from .models import Brand
from .serializers.common import BrandSerializer


class BrandListView(APIView):

    def get(self, _request):
        brands = Brand.objects.all()  
        serialized_products = BrandSerializer(brands, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)

    def post(self, request):
        brand_to_add = BrandSerializer(data=request.data)
        try:
            brand_to_add.is_valid()
            brand_to_add.save()
            return Response(brand_to_add.data, status=status.HTTP_201_CREATED)
        
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({ "detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      
        except:
            return Response({ "detail": "Unprocessable Entity" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class BrandDetailView(APIView):

    def get_brand(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise NotFound(detail="Can't find that brand!")

    def get(self, _request, pk):
        brand = self.get_brand(pk=pk) 
        serialized_brand = BrandSerializer(brand)
        return Response(serialized_brand.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        brand_to_edit = self.get_brand(pk=pk)
        updated_brand = BrandSerializer(brand_to_edit, data=request.data)
        try:
            updated_brand.is_valid()
            updated_brand.save()
            return Response(updated_brand.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        print('DELETE ME')
        album_to_delete = self.get_brand(pk=pk)
        album_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
