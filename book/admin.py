from django.contrib import admin
from .models import Publisher,Author,Book ,BookImage,Genre,Language
admin.site.register([
    Publisher,
    Author,
    Book,
    BookImage,
    Genre,
    Language
])
# Register your models here.
