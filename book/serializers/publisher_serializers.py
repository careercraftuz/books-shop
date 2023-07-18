from rest_framework.serializers import ModelSerializer
from book.models import Publisher

class PublisherSerializer(ModelSerializer):
    class Meta:
        model =  Publisher
        fields = '__all__'
