from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# List all books (GET /books/)
class BookListView(generics.ListAPIView):
    """
    List all books in the database.
    URL: /api/books/
    Method: GET
    Permission: No authentication required (public access)
    """
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer
    permission_classes = []  # Public access (no authentication required)

# Retrieve a single book (GET /books/<int:pk>/)
class BookDetailView(generics.RetrieveAPIView):
    
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer
    permission_classes = []  # Public access (no authentication required)

# Create a new book (POST /books/)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book

# Update an existing book (PUT/PATCH /books/<int:pk>/)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book

# Delete a book (DELETE /books/<int:pk>/)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book

