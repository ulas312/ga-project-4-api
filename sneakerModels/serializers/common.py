from rest_framework import serializers 
from ..models import SneakerModels 

class SneakerModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SneakerModels
        fields = '__all__'