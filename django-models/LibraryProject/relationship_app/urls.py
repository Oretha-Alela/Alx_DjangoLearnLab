from django.urls import path
from .views import list_books
from . import views

url_patterns = [
    path('books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]






