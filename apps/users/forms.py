#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__date__ = '2019/2/26 0026'
__author__ = 'liuqikui'

from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
