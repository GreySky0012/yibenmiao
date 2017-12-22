#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse

author = 'qiyue'


class HttpResponseUnauthorized(HttpResponse):
    status_code = 401
