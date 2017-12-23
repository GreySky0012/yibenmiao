#!/usr/bin/env python
# -*- coding: utf-8 -*-
author = 'qiyue'


class AccessControlAllowOrigin(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8080"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFtoken"
        response['Access-Control-Allow-Credentials'] = "true"
        return response
