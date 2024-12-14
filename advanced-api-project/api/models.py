from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    # name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # title of the book
    title = models.CharField(max_length=200)
    # year of publication
    publication_year = models.IntegerField()
    # Foreign key
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
