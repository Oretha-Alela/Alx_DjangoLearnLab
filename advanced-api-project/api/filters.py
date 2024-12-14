
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # Filtering by title (exact match)
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Title (contains)')
    # Filtering by publication year (exact match)
    publication_year = django_filters.NumberFilter(field_name='publication_year', lookup_expr='exact', label='Publication Year')
    # Filtering by author name (exact match)
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains', label='Author Name (contains)')
    
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author_name']  # Define filterable fields
