#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__date__ = ' 2019/9/2 0002 10:28'
__author__ = 'liuqikui'

from django.conf.urls import url, include
from .views import IndexView,DetailView
app_name='center'
urlpatterns = [
    url('^$',IndexView.as_view(),name='index'),
    url('detail/(?P<article_id>\d+)/$',DetailView.as_view(),name='detail')
]