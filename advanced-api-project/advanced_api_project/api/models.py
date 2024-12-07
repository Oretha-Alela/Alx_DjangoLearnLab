from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    # The name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # The author 
    title = models.CharField(max_length=200)
    # Publication Year
    publication_year = models.IntegerField()
    # Foreign key linking a book to an author
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
