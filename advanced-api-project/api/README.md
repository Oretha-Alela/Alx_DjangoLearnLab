# Advanced API Project - Book API Views

## List Books
- **URL:** `/api/books/`
- **Method:** `GET`
- **Permission:** Public (no authentication required)
- **Description:** Retrieves a list of all books.

## Retrieve a Book
- **URL:** `/api/books/<int:pk>/`
- **Method:** `GET`
- **Permission:** Public (no authentication required)
- **Description:** Retrieves a single book by its ID.

## Create a Book
- **URL:** `/api/books/create/`
- **Method:** `POST`
- **Permission:** Authenticated users only
- **Description:** Allows an authenticated user to create a new book.

## Update a Book
- **URL:** `/api/books/<int:pk>/update/`
- **Method:** `PUT`
- **Permission:** Authenticated users only
- **Description:** Allows an authenticated user to update an existing book.

## Delete a Book
- **URL:** `/api/books/<int:pk>/delete/`
- **Method:** `DELETE`
- **Permission:** Authenticated users only
- **Description:** Allows an authenticated user to delete a book.
