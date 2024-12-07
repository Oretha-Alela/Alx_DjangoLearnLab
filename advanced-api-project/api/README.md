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



# Advanced API - Book Model

## Features
This API supports the following features for the `Book` model:

### Filtering
- **`title`**: Filter books by title (e.g., `/api/books/?title=django`).
- **`publication_year`**: Filter books by publication year (e.g., `/api/books/?publication_year=2024`).
- **`author_name`**: Filter books by author's name (e.g., `/api/books/?author_name=John`).

### Searching
- Search across the `title` and `author_name` fields using the `search` parameter (e.g., `/api/books/?search=python`).

### Ordering
- Order results by `title` or `publication_year`. Use `-` for descending order (e.g., `/api/books/?ordering=-publication_year`).

## Example Requests

### Get all books with "django" in the title:
