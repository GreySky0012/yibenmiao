# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger("ybm")


def index(request):
    logger.info("request index")
    return HttpResponse(u'main page')
