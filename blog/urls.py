# -*- coding: utf-8 -*-
# @Author: klmp200
# @Date:   2016-06-04 23:24:06
# @Last Modified by:   klmp200
# @Last Modified time: 2016-06-04 23:40:24

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('blog.views',

    url(r'^$', 'blog', name='blog'),

)