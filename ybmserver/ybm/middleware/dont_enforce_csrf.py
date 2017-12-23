#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/23 18:06
# @Author  : Alex
# @Site    : 
# @File    : dont_enforce_csrf.py.py
# @Software: PyCharm


class DisableCSRFCheck(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

        response = self.get_response(request)

        return response
