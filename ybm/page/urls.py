#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

author = 'qiyue'

urlpatterns = [

    # page url
    url(r'^index/$', TemplateView.as_view(template_name="index.html")),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
