from .common import SneakerModelsSerializer
from brands.serializers.common import BrandSerializer
from comments.serializers.populated import PopulatedCommentSerializer
from jwt_auth.serializers.common import UserSerializer


class PopulatedSneakerModelsSerializer(SneakerModelsSerializer):
    brands = BrandSerializer(many=True)
    comments = PopulatedCommentSerializer(many=True)
    owner = UserSerializer()