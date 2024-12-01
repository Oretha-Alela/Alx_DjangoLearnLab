# Django API for Books

This API allows for CRUD operations on books.

## Endpoints

- `GET /books/`: List all books (No authentication required).
- `GET /books/<int:pk>/`: Get a single book by its ID (No authentication required).
- `POST /books/create/`: Create a new book (Authentication required).
- `PUT /books/<int:pk>/update/`: Update an existing book (Authentication required).
- `DELETE /books/<int:pk>/delete/`: Delete a book (Authentication required).

## Permissions
- `BookListView` and `BookDetailView` are publicly accessible.
- `BookCreateView`, `BookUpdateView`, and `BookDeleteView` are restricted to authenticated users only.




# Advanced Book API with Filtering, Searching, and Ordering

## Filtering
- `title`: Filter books by title (e.g., `/books/?title=Harry Potter`)
- `author`: Filter books by author (e.g., `/books/?author=J.K. Rowling`)
- `publication_year`: Filter books by publication year (e.g., `/books/?publication_year=2000`)

## Searching
- `search`: Search books by title or author (e.g., `/books/?search=Harry`)

## Ordering
- `ordering`: Order books by fields like `title` and `publication_year`
  - Use `-` for descending order (e.g., `/books/?ordering=-publication_year`)
