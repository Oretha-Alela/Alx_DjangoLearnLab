from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Model to represent an Author.
    Each Author has a name.

    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    """
    Model to represent a Book.
    Each Book has a title, publication year, and an associated Author.
    The relationship between Author and Book is one-to-many, where one Author
    can have multiple Books.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
