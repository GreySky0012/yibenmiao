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


class DisableCSRFCheck(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

        response = self.get_response(request)

        return response


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
