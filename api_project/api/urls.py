from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create the router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),  
]




from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

# Create the router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token retrieval endpoint
    path('', include(router.urls)),  # Include all routes registered with the router
]

