#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from ybm.apps.debug.views import debug

author = 'qiyue'

urlpatterns = [

    # app url
    url(r'^user/', include('ybm.apps.user.urls')),

    url('^debug/$', view=debug),
]
