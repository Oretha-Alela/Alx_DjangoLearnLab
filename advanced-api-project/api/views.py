from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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





from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  
from rest_framework.permissions import IsAuthenticated

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []
    
    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter  
    search_fields = ['title', 'author__name']  
    ordering_fields = ['title', 'publication_year']  
    ordering = ['title']  


from rest_framework.filters import SearchFilter

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []
    
    filter_backends = [DjangoFilterBackend, SearchFilter]  # Enable search along with filtering
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']  # Fields searchable in the API
    ordering_fields = ['title', 'publication_year']  # Fields by which the user can order results
    ordering = ['title']  # Default ordering


from rest_framework.filters import OrderingFilter

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of books with advanced filtering, searching, and ordering options.
    
    Query Parameters:
    - title: Filter books by title (case-insensitive).
    - publication_year: Filter books by exact publication year.
    - author_name: Filter books by author's name (case-insensitive).
    - search: Search across title and author name fields.
    - ordering: Order books by title or publication year. 
      Use '-field_name' for descending order (e.g., '-publication_year').
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Enable filtering, search, and ordering
    filterset_class = BookFilter  # Custom filter class
    search_fields = ['title', 'author__name']  # Fields searchable in the API
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title or publication year
    ordering = ['title']  # Default ordering by title

