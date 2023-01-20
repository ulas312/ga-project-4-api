from .common import BrandSerializer
from sneakerModels.serializers import SneakerModelsSerializer

class PopulatedBrandSerializer(BrandSerializer):
  sneaker_models = SneakerModelsSerializer(many=True)
