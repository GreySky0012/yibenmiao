# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from rest_framework.decorators import api_view

from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest

# Create your views here.
from ybm.settings import logger
from ybm.user.models import User
from ybm.utils.regular_util import is_email


def index(request, args):
    method = request.method
    if method == 'POST':
        return __add_user(request)
    elif method == 'GET':
        return __user_list(request)
    elif method == 'DELETE':
        return __delete_user(request)
    else:
        return HttpResponseNotFound('No such api with method %s' % method)


@api_view(['GET'])
def __user_list(request):
    users = User.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data)


@api_view(['POST'])
def __add_user(request):
    new_user = User(**json.loads(request.body))
    if new_user.name is None or new_user.phone_number is None:
        return HttpResponseBadRequest('name or user name can not be null')
    if not is_email(new_user.email):
        return HttpResponseBadRequest('email address is illegal')
    new_user.save()
    logger.info('add user' + new_user.name)
    return HttpResponse('user save success')


def __delete_user(request):

    logger.info('delete user')
    return HttpResponse('user delete success')
