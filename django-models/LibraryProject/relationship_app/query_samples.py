author = Author.objects.get(name=author_name)
books = author.books.all()