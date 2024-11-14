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