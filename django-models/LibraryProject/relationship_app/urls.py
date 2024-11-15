from django.urls import path
from .views import list_books
from . import views

url_patterns = [
    path('books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

# relationship_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    LogoutView.as_view(template_name=), LoginView.as_view(template_name=)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]



# Update the urls.py file

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]


 





