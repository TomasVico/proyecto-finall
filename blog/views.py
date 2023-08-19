from django.shortcuts import render, get_object_or_404,redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


def article_list(request):
    articles = Article.objects.all()
    form = ArticleForm()
    
    return render(request, 'blog/article_list.html', {'articles': articles, 'form': form, 'user': request.user})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save(commit=False)  
            form.instance.author = request.user  
            form.save()
            return redirect('article_list')  
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/delete_article.html', {'article': article})


def about(request):
    return render(request, 'blog/about.html')

def home(request):
    return render(request, 'blog/home.html')