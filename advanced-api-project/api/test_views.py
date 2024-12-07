
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Set up a test user and create a token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(title="Test Book", publication_year=2024, author=self.author)

        self.list_url = reverse('book-list')  # Assuming this is the endpoint for listing books
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})  # Assuming this is the endpoint for a single book

    def get_auth_headers(self):
        """Helper function to get authenticated headers."""
        return {'Authorization': f'Token {self.token.key}'}
    

    def test_create_book(self):
        """Test that a book can be created via the API."""
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id  # ForeignKey to Author model
        }

        response = self.client.post(self.list_url, data, format='json', HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Ensure a new book was created
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')  # Verify title of the created book


    def test_get_book(self):
        """Test that a single book can be retrieved via the API."""
        response = self.client.get(self.detail_url, HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')  # Verify the title in the response



    def test_update_book(self):
        """Test that a book can be updated via the API."""
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2025,
            'author': self.author.id
        }

        response = self.client.put(self.detail_url, data, format='json', HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.book.title, 'Updated Book Title')  # Verify the title was updated

    def test_delete_book(self):
        """Test that a book can be deleted via the API."""
        response = self.client.delete(self.detail_url, HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Ensure the book is deleted

    def test_filter_books_by_title(self):
        """Test that books can be filtered by title."""
        Book.objects.create(title='Another Book', publication_year=2024, author=self.author)
        response = self.client.get(self.list_url + '?title=Test', HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book with 'Test' in the title
    
    def test_search_books_by_author_name(self):
        """Test that books can be searched by author name."""
        Book.objects.create(title='Searchable Book', publication_year=2024, author=self.author)
        response = self.client.get(self.list_url + '?search=Author', HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure the search results are correct

    def test_order_books_by_publication_year(self):
        """Test that books can be ordered by publication year."""
        Book.objects.create(title='Older Book', publication_year=2020, author=self.author)
        response = self.client.get(self.list_url + '?ordering=publication_year', HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)  # Ensure the first book is the oldest

