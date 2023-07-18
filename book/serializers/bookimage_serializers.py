from rest_framework.serializers import ModelSerializer
from book.models import BookImage

class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = '__all__'