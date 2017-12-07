# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core import serializers
from django.http import HttpResponse

# Create your views here.
from ybm.settings import logger
from ybm.user.models import User


def index(request, args):
    return HttpResponse('user index')


def user_list(request, args):
    users = User.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data)


def add(request, args):
    new_user = User(**json.loads(args))
    new_user.save()
    logger.info('add user' + new_user.name)
    return HttpResponse('user save success')
