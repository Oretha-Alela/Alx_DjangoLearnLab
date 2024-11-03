# Create a book instance with the code
from bookshelf.models import Book
Book.objects.create
book_1 = Book(title='1984',author='George Orwell', publication_year='1949')
print("Book Created:", book_1)


# a book with the given characteristics should be created in the database
# Expected output is "Book created: Book object (1)


