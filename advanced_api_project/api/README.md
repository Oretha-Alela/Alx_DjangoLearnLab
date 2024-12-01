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
