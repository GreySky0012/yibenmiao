#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from ybm.apps.user.views import index

author = 'qiyue'

urlpatterns = [

    # app url
    url(r'^user/', include('ybm.apps.user.urls')),
]
