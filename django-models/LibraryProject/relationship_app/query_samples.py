author = Author.objects.get(name=author_name)
books = author.books.all()

Library.objects.get(name=library_name)