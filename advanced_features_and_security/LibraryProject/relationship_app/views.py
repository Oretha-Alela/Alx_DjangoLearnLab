from django.shortcuts import render
from .models import Book



# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books':books}
    return render(request, relationship_app/list_books.html, context)

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = relationship_app/library_detail.html

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    library = self.get_object()
    context['books'] = library.books.all()
    return context



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Registration View (custom view)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page after successful registration
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})




# create the views

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# check user roles
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (only accessible by Admins)
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view (only accessible by Librarians)
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view (only accessible by Members)
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# relationship_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Assuming you have a BookForm for adding/editing books

# View to add a new book, restricted to users with 'can_add_book' permission
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a page listing all books
    else:
        form = BookForm()
    
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit an existing book, restricted to users with 'can_change_book' permission
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a page listing all books
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# View to delete a book, restricted to users with 'can_delete_book' permission
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to a page listing all books
    
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})






from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required
from .models import Article

# View to create a new article
@permission_required('app_name.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content, author=request.user)
        return render(request, 'article_list.html')  # redirect to a list of articles
    return render(request, 'create_article.html')

# View to edit an article
@permission_required('app_name.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return render(request, 'article_list.html')  # redirect to a list of articles
    return render(request, 'edit_article.html', {'article': article})

# View to delete an article
@permission_required('app_name.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return render(request, 'article_list.html')  # redirect to a list of articles

# View to list articles (accessible by anyone with can_view permission)
@permission_required('app_name.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})
