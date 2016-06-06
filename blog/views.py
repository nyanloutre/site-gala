#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from blog.models import Article


def blog(request):

    articles = Article.objects.exclude(published=False).order_by('-date')
    return render(request, 'blog/blog.html', {'articles': articles})


def article(request, slug):

    article = get_object_or_404(Article, slug=slug, published=True)

    return render(request, 'blog/article.html', {'article': article})
