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

