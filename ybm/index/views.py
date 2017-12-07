# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponse

# Create your views here.
from ybm.settings import logger


def index(request):
    logger.info("request index")
    return HttpResponse(u'main page')
