from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError

from .serializers.populated import PopulatedSneakerModelsSerializer
from .serializers.common import SneakerModelsSerializer
from .models import SneakerModels


class SneakerModelsListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, _request):
        sneaker_models = SneakerModels.objects.all()
        serialized_sneaker_models = SneakerModelsSerializer(sneaker_models, many=True)
        return Response(serialized_sneaker_models.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        model_to_add = SneakerModelsSerializer(data=request.data)
        try:
            model_to_add.is_valid()
            model_to_add.save()
            return Response(model_to_add.data, status=status.HTTP_201_CREATED)
        
        except IntegrityError as e:
            res = {
                "detail": str(e)
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except AssertionError as e:
            return Response({ "detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      
        except:
            return Response({ "detail": "Unprocessable Entity" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SneakerModelsDetailView(APIView):

    def get_sneaker_model(self, pk):
        try:
            return SneakerModels.objects.get(pk=pk)
        except SneakerModels.DoesNotExist:
            raise NotFound(detail="Can't find that sneaker model!")

    def get(self, _request, pk):
        sneaker_model = self.get_sneaker_model(pk=pk) 
        serialized_sneaker_model = SneakerModelsSerializer(sneaker_model)
        return Response(serialized_sneaker_model.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        sneaker_model_to_edit = self.get_sneaker_model(pk=pk)
        updated_sneaker_model = SneakerModelsSerializer(sneaker_model_to_edit, data=request.data)
        try:
            updated_sneaker_model.is_valid()
            updated_sneaker_model.save()
            return Response(updated_sneaker_model.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        print('DELETE ME')
        sneaker_model_to_delete = self.get_sneaker_model(pk=pk)
        sneaker_model_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

