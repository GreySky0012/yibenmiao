# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core import serializers
from django.http import *

# Create your views here.
from rest_framework.decorators import api_view

from ybm.apps.blog.models import Blog


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def index(request):
    method = request.method
    if method == 'GET':
        return get_all_blog(request)
    elif method == 'PUT':
        return save_blog(request)
    else:
        return HttpResponseNotFound(json.dumps({'error': 'No such api with method %s' % method}),
                                    content_type="application/json")


def get_all_blog(request):
    try:
        blogs = Blog.objects.all()
        return HttpResponse(json.dumps({'blogs': blogs}),
                            content_type="application/json")
    except BaseException as e:
        return HttpResponseServerError(json.dumps({'error': e}),
                                       content_type="application/json")


def save_blog(request):
    try:
        blog = Blog(author='hhr')
        blog.save()
        return HttpResponse(json.dumps({'result': 'save blog ok'}),
                            content_type="application/json")
    except BaseException as e:
        return HttpResponseServerError(json.dumps({'error': e}),
                                       content_type="application/json")
