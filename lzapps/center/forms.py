#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__date__ = ' 2019/8/29 0029 13:03'
__author__ = 'liuqikui'

from django import forms

class ArticleForm(forms.Form):
    pass


class ProgramForm(forms.Form):
    program_title = forms.CharField(required=True)
    program_desc = forms.CharField(max_length=50)
    domain_name = forms.CharField(max_length=50)
    skin = forms.CharField(max_length=20)
    first_letter = forms.CharField(max_length=6)
    specialUrl = forms.CharField(max_length=100)
    program_pic_url = forms.ImageField(max_length=100)
