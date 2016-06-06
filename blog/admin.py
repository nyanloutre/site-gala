from django.db import models
from django.contrib import admin

from markdownx.models import MarkdownxField
from markdownx.widgets import AdminMarkdownxWidget
from ordered_model.admin import OrderedModelAdmin

from .models import Article, Page


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget},
    }

    list_display = ('title', 'published', 'date')
    list_editable = ('title', 'published')
    ordering = ('-date', )
    search_fields = ['title', 'content', 'date']


class PageAdmin(OrderedModelAdmin):
    formfield_overrides = {
        MarkdownxField: {'widget': AdminMarkdownxWidget},
    }

    list_display = ('title', 'published', 'date', 'move_up_down_links')
    list_editable = ('title', 'published')
    search_fields = ['title', 'content', 'date']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Page, PageAdmin)
