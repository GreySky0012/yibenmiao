#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse

author = 'qiyue'


def index(request):
    return HttpResponse('ybm api server')


def debug(request):
    return HttpResponse('debug api')
