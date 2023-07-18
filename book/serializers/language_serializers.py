from rest_framework.serializers import ModelSerializer
from book.models import Language

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
        