#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from ybm.apps.user.views import index, sign_in

author = 'qiyue'

urlpatterns = [

    # user url
    url(r'^$', index),
    url(r'sign_in/$', sign_in),
]
