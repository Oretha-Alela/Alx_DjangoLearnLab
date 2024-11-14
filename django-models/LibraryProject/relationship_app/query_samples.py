import django
import os
from django.conf import settings

# Set up Django settings for standalone script usage
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        for book in books:
            print(f"Book: {book.title}")
    except Author.DoesNotExist:
        print(f"Author with name {author_name} does not exist.")

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"Book: {book.title}")
    except Library.DoesNotExist:
        print(f"Library with name {library_name} does not exist.")

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library with name {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library {library_name}.")