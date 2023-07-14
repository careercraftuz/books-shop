from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Language(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    cover_choices = [
        ('HC', 'Hardcover'),
        ('PB', 'Paperback'),
        ('EB', 'E-book'),
    ]
    font_shrift_choices = [
        ('LOTIN', 'Lotin'),
        ('CYRILLIC', 'Cyrillic'),
    ]
    paper_format_choices = [
        ('A4', 'A4'),
        ('A5', 'A5'),
    ]

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    description = models.TextField(null=True, blank=True)
    cover = models.CharField(max_length=20, choices=cover_choices, default='HC')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    font_shrift = models.CharField(max_length=20, choices=font_shrift_choices, default='LOTIN')
    paper_format = models.CharField(max_length=20, choices=paper_format_choices, default='A4')

    def __str__(self):
        return self.title


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_images')

    def __str__(self):
        return self.book.title
        