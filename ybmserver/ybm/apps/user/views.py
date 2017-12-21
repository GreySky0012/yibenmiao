# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError, \
    HttpResponseForbidden
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from ybm.apps.user.models import UserInfo
from ybm.settings import logger
from ybm.utils.EncryUtil import md5
from ybm.utils.regular_util import is_email, is_tel_phone_number


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def index(request):
    method = request.method
    if method == 'POST':
        return __add_user(request)
    elif method == 'GET':
        return __user_list(request)
    elif method == 'DELETE':
        return __delete_user(request)
    else:
        return HttpResponseNotFound('No such api with method %s' % method)


def __user_list(request):
    users = UserInfo.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data)


def __add_user(request):
    try:
        new_user = UserInfo(**json.loads(request.body))
        if new_user.username is None or \
                new_user.phone_number is None or \
                new_user.password is None:
            return HttpResponseBadRequest('name, phone number or password can not be null.')
        if not is_email(new_user.email):
            return HttpResponseBadRequest('email address is illegal.')
        if not is_tel_phone_number(new_user.phone_number):
            return HttpResponseBadRequest('phone number is illegal.')
        if new_user.username.__len__() > 20:
            return HttpResponseBadRequest('name too long.')
        UserInfo.objects.create_user(username=new_user.username,
                                     email=new_user.email,
                                     password=new_user.password,
                                     phone_number=new_user.phone_number)
        # new_user.password = md5(new_user.password)
        # new_user.save()
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(e)
    logger.info('add user ' + new_user.username)
    return HttpResponse('user save success')


def __delete_user(request):
    try:
        user_id = int(request.GET.get("id"))
        UserInfo.objects.filter(id=user_id).delete()
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(e)
    logger.info('delete user : ' + str(user_id))
    return HttpResponse('user delete success')


@api_view(['POST'])
def sign_in(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                logger.info('user %s login ' % username)
                login(request, user)
                return HttpResponse(json.dumps({'username': user.username}), content_type="application/json")
            else:
                logger.warning('user %s is not active ' % username)
                return HttpResponseForbidden('user is not active')
        else:
            return HttpResponseForbidden('username or password error')
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(e)
