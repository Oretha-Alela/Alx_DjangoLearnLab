# All books by a specific author
author = Author.objects.get(name=author_name)
books = author.books.all()

# List all books in a library
Library.objects.get(name=library_name)

objects.filter(author=author)

# Retrieve the librarian for a library

Librarian.objects.get(library=library_name)