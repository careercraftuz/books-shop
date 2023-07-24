from rest_framework.serializers import ModelSerializer
from book.models import Author,Book,BookImage,Genre,Language,Publisher

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'



class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class BookImageSerializer(ModelSerializer):
    class Meta:
        model = BookImage
        fields = '__all__'



class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'



class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'



class PublisherSerializer(ModelSerializer):
    class Meta:
        model =  Publisher
        fields = '__all__'