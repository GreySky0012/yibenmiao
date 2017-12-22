#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from ybm.apps.blog.views import *

author = 'qiyue'

urlpatterns = [

    # user url
    url(r'^$', index),
]
