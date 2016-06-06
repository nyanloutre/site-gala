# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True)),
                ('content', markdownx.models.MarkdownxField(verbose_name='Contenu')),
                ('published', models.BooleanField(default=False, verbose_name='Publication')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('slug', models.SlugField(editable=False, max_length=150, unique=True)),
                ('content', markdownx.models.MarkdownxField(verbose_name='Contenu')),
                ('published', models.BooleanField(default=False, verbose_name='Publication')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
            ],
        ),
    ]
