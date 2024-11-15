from django.shortcuts import render
from .models import Book


# Create your views here.
def book_list(request):
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
