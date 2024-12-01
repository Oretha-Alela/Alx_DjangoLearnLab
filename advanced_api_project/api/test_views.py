from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        self.book_author = Author.objects.create(name="J.K. Rowling")
        
        # Create a book
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.book_author
        )

        # Define the URLs for the endpoints
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        # Test creating a new book
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
            "author": self.book_author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Check if the book count increased
        self.assertEqual(Book.objects.last().title, "Harry Potter and the Chamber of Secrets")

    def test_get_books(self):
        # Test retrieving the list of books
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only 1 book initially

    def test_get_book_detail(self):
        # Test retrieving a single book by ID
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        # Test updating an existing book
        data = {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "publication_year": 1999,
            "author": self.book_author.id
        }
        response = self.client.put(self.book_detail_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Refresh the book from the DB
        self.assertEqual(self.book.title, "Harry Potter and the Prisoner of Azkaban")

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Book should be deleted

    def test_filter_books_by_title(self):
        # Test filtering books by title
        Book.objects.create(
            title="Harry Potter and the Goblet of Fire",
            publication_year=2000,
            author=self.book_author
        )
        response = self.client.get(self.book_list_url + '?title=Goblet')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only 1 book with 'Goblet' in title

    def test_search_books_by_author(self):
        # Test searching books by author
        response = self.client.get(self.book_list_url + '?search=Rowling')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books by 'Rowling'

    def test_order_books_by_publication_year(self):
        # Test ordering books by publication year
        Book.objects.create(
            title="Harry Potter and the Half-Blood Prince",
            publication_year=2005,
            author=self.book_author
        )
        response = self.client.get(self.book_list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # First book should have the earliest year

    def test_permission_required_for_create(self):
        # Test that only authenticated users can create a book
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.book_author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Now, log in and try again
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
