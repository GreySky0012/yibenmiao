# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
import logging
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger("ybm")


def index(request,args):
    logger.info("request index")
    return HttpResponse(u'main page')
