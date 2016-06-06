from django.db import models
from django.utils.text import slugify
from blog.snippets import SlugUnique
from django.core.urlresolvers import reverse
from markdownx.models import MarkdownxField


class Article(models.Model):

    """Classe article"""

    title = models.CharField(max_length=100, verbose_name="Titre")
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    content = MarkdownxField(verbose_name="Contenu")
    published = models.BooleanField(default=False, verbose_name="Publication")
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        SlugUnique.unique_slugify(self, self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article', args=[self.slug])
