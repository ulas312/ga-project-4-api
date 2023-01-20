from rest_framework import serializers
from .common import SneakerModelsSerializer
from brands.serializers.common import BrandSerializer
from comments.serializers.common import CommentSerializer


class PopulatedSneakerModelsSerializer(SneakerModelsSerializer):
    brands = BrandSerializer(many=True)
    # sneakerModels = SneakerModelsSerializer(many=True)
    comments = CommentSerializer(many=True)