# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view

from django.http import HttpResponse

# Create your views here.
from ybm.settings import logger


@api_view(['GET'])
def index(request):
    logger.info("request index")
    return HttpResponse(u'main page')
