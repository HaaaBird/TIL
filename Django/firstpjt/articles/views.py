from django.shortcuts import render, redirect
from .models import Article
import random
from .forms import ArticleForm
# Create your views here.


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def index(request):
    papers = Article.objects.all()
    context = {
        'papers':papers
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [
        '국밥1',
        '국밥12222',
        '국밥133333',
        '국밥144444',
        '국밥15555',
    ]
    picked = random.choice(foods)
    context = {
        'foods':foods,
        'picked':picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/serach.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)