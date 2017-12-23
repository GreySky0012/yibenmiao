# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError, \
    HttpResponseForbidden
from rest_framework.decorators import api_view

# Create your views here.
from ybm.apps.user.models import UserInfo
from ybm.http.response import HttpResponseUnauthorized
from ybm.settings import logger
from ybm.utils.EncryUtil import md5
from ybm.utils.regular_util import is_email, is_tel_phone_number


def csrf_disable(view_func):
    """
    Marks a view function as being exempt from the CSRF view protection.
    """
    # We could just do view_func.csrf_exempt = True, but decorators
    # are nicer if they don't have side-effects, so we return a new
    # function.
    def wrapped_view(*args, **kwargs):
        setattr(args[0], '_dont_enforce_csrf_checks', True)
        return view_func(*args, **kwargs)
    wrapped_view.csrf_exempt = True
    return wrapped_view


@csrf_disable
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
        return HttpResponseNotFound(json.dumps({'detail': 'No such api with method %s' % method}),
                                    content_type="application/json")


def __user_list(request):
    users = UserInfo.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data)


def __add_user(request):
    try:
        print(request.data)
        new_user = UserInfo(**request.data)
        print(new_user)
        if new_user.username is None or \
                new_user.phone_number is None or \
                new_user.password is None:
            return HttpResponseBadRequest(json.dumps({'detail': 'name, phone number or password can not be null.'}),
                                          content_type="application/json")
        if not is_email(new_user.email):
            return HttpResponseBadRequest(json.dumps({'detail': 'email address is illegal.'}),
                                          content_type="application/json")
        if not is_tel_phone_number(new_user.phone_number):
            return HttpResponseBadRequest(json.dumps({'detail': 'phone number is illegal.'}),
                                          content_type="application/json")
        if new_user.username.__len__() > 20:
            return HttpResponseBadRequest(json.dumps({'detail': 'name too long'}),
                                          content_type="application/json")

        UserInfo.objects.create_user(username=new_user.username,
                                     email=new_user.email,
                                     password=new_user.password,
                                     phone_number=new_user.phone_number)
        # new_user.password = md5(new_user.password)
        # new_user.save()
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'detail': e}),
                                       content_type="application/json")

    logger.info('add user ' + new_user.username)
    return HttpResponse(json.dumps({'result': 'user save success'}))


def __delete_user(request):
    try:
        user_id = int(request.data.get("id"))
        UserInfo.objects.filter(id=user_id).delete()
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'detail': e}))
    logger.info('delete user : ' + str(user_id))
    return HttpResponse(json.dumps({'detail': 'user delete success'}),
                        content_type="application/json")


@csrf_disable
@api_view(['POST'])
def sign_in(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                logger.info('user %s login ' % username)
                login(request, user)
                return HttpResponse(json.dumps({'username': user.username}),
                                    content_type="application/json")
            else:
                logger.warning('user %s is not active ' % username)
                return HttpResponseUnauthorized(json.dumps({'detail': 'user is not active'}),
                                                content_type="application/json")
        else:
            return HttpResponseUnauthorized(json.dumps({'detail': 'username or password error'}),
                                            content_type="application/json")
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'detail': e}), content_type="application/json")


@csrf_disable
@api_view(['POST'])
def check_username(request):
    try:
        user_name = request.data.get("username")
        logger.debug('check username : %s.' % user_name)
        user = UserInfo.objects.filter(username=user_name)
        if user.__len__() == 0:
            return HttpResponse(json.dumps({'result': 'OK'}))
        else:
            return HttpResponse(json.dumps({'result': 'FAILED'}))
    except BaseException as e:
        logger.exception(e)
        return HttpResponseServerError(json.dumps({'detail': e}),
                                       content_type="application/json")