from django.shortcuts import render

# Create your views here.
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
"book_list", "books"