#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__date__ = ' 2019/8/29 0029 16:28'
__author__ = 'liuqikui'

import xadmin
from .models import Program, CenterArticle, CenterHeadLine


class ProgramAdmin(object):
    list_display = ('program_title', 'parent', 'isleaf', 'is_avail')
    ordering = ('-frequency',)


class CenterArticleAdmin(object):
    list_display = ('id','title', 'program', 'data_entry_staffer', 'is_avail', 'source')
    list_filter = ('title', 'data_entry_staffer', 'author', 'editor',  'source')
    search_fields = ('title', 'data_entry_staffer', 'author', 'editor', 'source')
    ordering = ('-date_issued',)


class CenterHeadLineAdmin(object):
    list_display = ('title', 'article', 'photo_url', 'sign', 'top_program_id')
    ordering = ('-operate_time',)

xadmin.site.register(Program, ProgramAdmin)
xadmin.site.register(CenterArticle, CenterArticleAdmin)
xadmin.site.register(CenterHeadLine, CenterHeadLineAdmin)
