#-*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import Article


def blog(request):

    articles = Article.objects.exclude(published=False).order_by('-date')
    return render(request, 'blog/blog.html', {'articles': articles})
