from .common import SneakerModelsSerializer
from brands.serializers.common import BrandSerializer
from comments.serializers.populated import PopulatedCommentSerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedSneakerModelsSerializer(SneakerModelsSerializer):
    brand = BrandSerializer(many=True)
    comments = PopulatedCommentSerializer(many=True)
    owner = UserSerializer()