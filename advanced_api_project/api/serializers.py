
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    This serializer includes a custom validation for the publication year
    to ensure that it is not in the future.
    """
    def validate_publication_year(self, value):
        if value > 2024:  # Change to the current year dynamically if needed
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    This serializer includes a nested BookSerializer to return related
    books when an Author is serialized.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
