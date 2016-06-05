from django.db import models
from django.contrib import admin

from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget},
    }

    list_display = ('title', 'published', 'date')
    list_editable = ('title', 'published')
    ordering = ('-date', )
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
