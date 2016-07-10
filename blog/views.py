#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from blog.models import Article, Page


def blog(request):

    articles = Article.objects.exclude(published=False).order_by('-date')
    return render(request, 'blog/blog.html',
                  {'articles': articles, 'nav': get_nav(request)})


def article(request, slug):

    article = get_object_or_404(Article, slug=slug, published=True)

    return render(request, 'blog/article.html',
                  {'article': article, 'nav': get_nav(request)})


def page(request, slug):

    content = get_object_or_404(Page, slug=slug, published=True)

    return render(request, 'blog/page.html',
                  {'content': content, 'nav': get_nav(request)})


def get_nav(request):

    nav = {
        'pages': Page.objects.exclude(published=False).order_by('order'),
        'index': reverse('blog'),
        'path': request.path
    }

    return nav
