from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Step 2: Customize the Admin Interface
    list_display = ('title', 'author', 'publication_year')  # Display these fields in the list view
    search_fields = ('title', 'author')  # Enable search functionality on title and author
    list_filter = ('publication_year',)  # Enable filtering by publication year
