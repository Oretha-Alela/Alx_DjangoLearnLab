from django.urls import path
from .views import list_books
from . import views

url_patterns = [
    path('books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

<!-- relationship_app/templates/relationship_app/list_books.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of Books</title>
</head>
<body>
    <h1>Books Available:</h1>
    <ul>
        {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>




<!-- relationship_app/templates/relationship_app/library_detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library Detail</title>
</head>
<body>
    <h1>Library: {{ library.name }}</h1>
    <h2>Books in Library:</h2>
    <ul>
        {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }} (Published {{ book.publication_year }})</li>
        {% endfor %}
    </ul>
</body>
</html>