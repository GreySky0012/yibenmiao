# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

def index(request,args):
    return HttpResponse('URL错误')

def Test(request,args):
    return HttpResponse('测试接口')