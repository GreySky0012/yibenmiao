# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError, \
    HttpResponseForbidden
from rest_framework.decorators import api_view

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
        return HttpResponseNotFound(json.dumps({'error': 'No such api with method %s' % method}),
                                    content_type="application/json")


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
            return HttpResponseBadRequest(json.dumps({'error': 'name, phone number or password can not be null.'}),
                                          content_type="application/json")
        if not is_email(new_user.email):
            return HttpResponseBadRequest(json.dumps({'error': 'email address is illegal.'}),
                                          content_type="application/json")
        if not is_tel_phone_number(new_user.phone_number):
            return HttpResponseBadRequest(json.dumps({'error': 'phone number is illegal.'}),
                                          content_type="application/json")
        if new_user.username.__len__() > 20:
            return HttpResponseBadRequest(json.dumps({'error': 'name too long'}),
                                          content_type="application/json")

        UserInfo.objects.create_user(username=new_user.username,
                                     email=new_user.email,
                                     password=new_user.password,
                                     phone_number=new_user.phone_number)
        # new_user.password = md5(new_user.password)
        # new_user.save()
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'error': e}),
                                       content_type="application/json")

    logger.info('add user ' + new_user.username)
    return HttpResponse(json.dumps({'result': 'user save success'}))


def __delete_user(request):
    try:
        user_id = int(request.GET.get("id"))
        UserInfo.objects.filter(id=user_id).delete()
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'error': e}))
    logger.info('delete user : ' + str(user_id))
    return HttpResponse(json.dumps({'error': 'user delete success'}),
                        content_type="application/json")


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
                return HttpResponse(json.dumps({'username': user.username}),
                                    content_type="application/json")
            else:
                logger.warning('user %s is not active ' % username)
                return HttpResponseForbidden(json.dumps({'error': 'user is not active'}),
                                             content_type="application/json")
        else:
            return HttpResponseForbidden(json.dumps({'error': 'username or password error'},
                                                    content_type="application/json"))
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'error': e}), content_type="application/json")


@api_view(['POST'])
def check_username(request):
    try:
        user_name = request.GET.get("username")
        logger.debug('check username : %s.' % user_name)
        user = UserInfo.objects.filter(username=user_name)
        if user.__len__() == 0:
            return HttpResponse(json.dumps({'result': 'OK'}))
        else:
            return HttpResponse(json.dumps({'result': 'FAILED'}))
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'error': e}),
                                       content_type="application/json")
